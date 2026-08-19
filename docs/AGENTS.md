# Agentes

O fluxo usa LangChain `create_agent` para sete papéis e LangGraph para garantir a ordem de execução:

1. `roteador`: classifica intenção e não responde tecnicamente;
2. `ativos_solares`: usa RAG para componentes, eficiência e ambiente;
3. `manutencao`: orienta sobre manutenção e relatórios, sem registrar operações;
4. `seguranca`: recusa práticas inseguras e reforça controles aplicáveis;
5. `faq_apolloai`: explica identidade, escopo e limitações;
6. `juiz_factual`: produz decisão estruturada, aprova, corrige ou rejeita;
7. `orquestrador`: consolida somente conteúdo aprovado.

Classificadores e guardrails determinísticos não entram nessa contagem. Perguntas bloqueadas terminam antes do roteador. Perguntas fora do escopo terminam depois do roteador sem chamar especialista. Respostas técnicas sempre passam pelo juiz.
