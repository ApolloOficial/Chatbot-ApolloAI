#!/usr/bin/env bash
set -euo pipefail

AWS_REGION="${AWS_REGION:-us-east-1}"
AWS_DEFAULT_REGION="$AWS_REGION"
INSTANCE_NAME="${INSTANCE_NAME:-apolloai-k3s}"
INSTANCE_TYPE="${INSTANCE_TYPE:-t3.small}"
INSTANCE_PROFILE_NAME="${INSTANCE_PROFILE_NAME:-LabInstanceProfile}"
SECURITY_GROUP_NAME="${SECURITY_GROUP_NAME:-apolloai-k3s-sg}"
KEY_NAME="${KEY_NAME:-apolloai-cloudshell}"
KEY_PATH="${KEY_PATH:-$HOME/.ssh/${KEY_NAME}.pem}"
AMI_PARAMETER="/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64"

export AWS_REGION AWS_DEFAULT_REGION

for command in aws curl; do
  if ! command -v "$command" >/dev/null; then
    echo "$command não está instalado." >&2
    exit 1
  fi
done

ACCOUNT_ID="$(aws sts get-caller-identity --query Account --output text)"
CALLER_ARN="$(aws sts get-caller-identity --query Arn --output text)"
echo "Conta AWS: $ACCOUNT_ID"
echo "Identidade: $CALLER_ARN"
echo "Região: $AWS_REGION"

VPC_ID="$(aws ec2 describe-vpcs \
  --filters Name=is-default,Values=true \
  --query 'Vpcs[0].VpcId' \
  --output text)"
if [[ -z "$VPC_ID" || "$VPC_ID" == "None" ]]; then
  echo "A região $AWS_REGION não possui VPC padrão." >&2
  exit 1
fi

SUBNET_ID="$(aws ec2 describe-subnets \
  --filters Name=vpc-id,Values="$VPC_ID" Name=default-for-az,Values=true \
  --query 'Subnets[0].SubnetId' \
  --output text)"
if [[ -z "$SUBNET_ID" || "$SUBNET_ID" == "None" ]]; then
  echo "Nenhuma subnet padrão foi encontrada na VPC $VPC_ID." >&2
  exit 1
fi

SECURITY_GROUP_ID="$(aws ec2 describe-security-groups \
  --filters Name=vpc-id,Values="$VPC_ID" Name=group-name,Values="$SECURITY_GROUP_NAME" \
  --query 'SecurityGroups[0].GroupId' \
  --output text)"
if [[ -z "$SECURITY_GROUP_ID" || "$SECURITY_GROUP_ID" == "None" ]]; then
  SECURITY_GROUP_ID="$(aws ec2 create-security-group \
    --group-name "$SECURITY_GROUP_NAME" \
    --description "ApolloAI K3s ingress" \
    --vpc-id "$VPC_ID" \
    --query GroupId \
    --output text)"
fi

authorize_ingress() {
  local port="$1"
  local cidr="$2"
  local error
  if ! error="$(aws ec2 authorize-security-group-ingress \
    --group-id "$SECURITY_GROUP_ID" \
    --protocol tcp \
    --port "$port" \
    --cidr "$cidr" \
    2>&1)"; then
    if [[ "$error" != *"InvalidPermission.Duplicate"* ]]; then
      echo "$error" >&2
      exit 1
    fi
  fi
}

CLOUDSHELL_IP="$(curl --fail --silent --show-error https://checkip.amazonaws.com | tr -d '[:space:]')"
if [[ ! "$CLOUDSHELL_IP" =~ ^([0-9]{1,3}\.){3}[0-9]{1,3}$ ]]; then
  echo "Não foi possível identificar o IPv4 público do CloudShell." >&2
  exit 1
fi

authorize_ingress 22 "$CLOUDSHELL_IP/32"
authorize_ingress 80 0.0.0.0/0
authorize_ingress 443 0.0.0.0/0

mkdir -p "$(dirname "$KEY_PATH")"
chmod 700 "$(dirname "$KEY_PATH")"
if aws ec2 describe-key-pairs --key-names "$KEY_NAME" >/dev/null 2>&1; then
  if [[ ! -f "$KEY_PATH" ]]; then
    echo "O key pair $KEY_NAME existe na AWS, mas $KEY_PATH não existe no CloudShell." >&2
    echo "Execute novamente com outro nome, por exemplo KEY_NAME=apolloai-cloudshell-2." >&2
    exit 1
  fi
else
  if [[ -e "$KEY_PATH" ]]; then
    mv "$KEY_PATH" "${KEY_PATH}.stale-$(date +%Y%m%d%H%M%S)"
  fi
  aws ec2 create-key-pair \
    --key-name "$KEY_NAME" \
    --key-type ed25519 \
    --query KeyMaterial \
    --output text >"$KEY_PATH"
fi
chmod 400 "$KEY_PATH"

EXISTING_INSTANCE_ID="$(aws ec2 describe-instances \
  --filters \
    Name=tag:Name,Values="$INSTANCE_NAME" \
    Name=instance-state-name,Values=pending,running,stopping,stopped \
  --query 'Reservations[0].Instances[0].InstanceId' \
  --output text)"

if [[ -n "$EXISTING_INSTANCE_ID" && "$EXISTING_INSTANCE_ID" != "None" ]]; then
  INSTANCE_ID="$EXISTING_INSTANCE_ID"
  STATE="$(aws ec2 describe-instances \
    --instance-ids "$INSTANCE_ID" \
    --query 'Reservations[0].Instances[0].State.Name' \
    --output text)"
  if [[ "$STATE" == "stopped" ]]; then
    aws ec2 start-instances --instance-ids "$INSTANCE_ID" >/dev/null
  elif [[ "$STATE" == "stopping" ]]; then
    aws ec2 wait instance-stopped --instance-ids "$INSTANCE_ID"
    aws ec2 start-instances --instance-ids "$INSTANCE_ID" >/dev/null
  fi
else
  AMI_ID="$(aws ssm get-parameter \
    --name "$AMI_PARAMETER" \
    --query Parameter.Value \
    --output text)"
  USER_DATA="$(mktemp)"
  trap 'rm -f -- "$USER_DATA"' EXIT
  cat >"$USER_DATA" <<'USERDATA'
#!/usr/bin/env bash
set -euxo pipefail
dnf install -y docker git
systemctl enable --now docker
usermod -aG docker ec2-user
USERDATA

  INSTANCE_ID="$(aws ec2 run-instances \
    --image-id "$AMI_ID" \
    --instance-type "$INSTANCE_TYPE" \
    --key-name "$KEY_NAME" \
    --iam-instance-profile Name="$INSTANCE_PROFILE_NAME" \
    --network-interfaces "DeviceIndex=0,SubnetId=${SUBNET_ID},Groups=${SECURITY_GROUP_ID},AssociatePublicIpAddress=true" \
    --block-device-mappings 'DeviceName=/dev/xvda,Ebs={VolumeSize=8,VolumeType=gp3,DeleteOnTermination=true}' \
    --credit-specification CpuCredits=standard \
    --metadata-options HttpTokens=required,HttpEndpoint=enabled \
    --user-data "file://${USER_DATA}" \
    --tag-specifications \
      "ResourceType=instance,Tags=[{Key=Name,Value=${INSTANCE_NAME}},{Key=Project,Value=ApolloAI}]" \
      "ResourceType=volume,Tags=[{Key=Name,Value=${INSTANCE_NAME}},{Key=Project,Value=ApolloAI}]" \
    --query 'Instances[0].InstanceId' \
    --output text)"
fi

aws ec2 wait instance-running --instance-ids "$INSTANCE_ID"
aws ec2 wait instance-status-ok --instance-ids "$INSTANCE_ID"
PUBLIC_IP="$(aws ec2 describe-instances \
  --instance-ids "$INSTANCE_ID" \
  --query 'Reservations[0].Instances[0].PublicIpAddress' \
  --output text)"

echo "Instância: $INSTANCE_ID"
echo "IPv4 público: $PUBLIC_IP"
echo "Security Group: $SECURITY_GROUP_ID"
echo "Chave privada: $KEY_PATH"
echo "Conecte com: ssh -i $KEY_PATH ec2-user@$PUBLIC_IP"
