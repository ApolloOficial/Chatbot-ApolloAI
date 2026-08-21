# Guardrails e juiz factual

O guardrail de entrada aplica verificações baratas primeiro: prompt injection, acesso a dados internos, ofensa e prática perigosa. Em seguida, saudações, agradecimentos, despedidas e interações sociais breves recebem uma resposta educada pela rota `faq_apolloai`, sem depender do classificador semântico. A correspondência exige que toda a mensagem seja social; por isso, começar uma tentativa de injeção ou um comando perigoso com “oi” não contorna as verificações. Temas explicitamente fora do escopo continuam bloqueados e as demais mensagens passam pela classificação semântica. Perguntas legítimas de segurança são permitidas.

O juiz recebe rascunho e exatamente as fontes recuperadas. Sua decisão Pydantic contém aprovação/correção/rejeição, fundamentação, segurança, escopo, validade das fontes, possível hipótese tratada como diagnóstico, motivos e eventual resposta corrigida. Decisão inválida falha de modo fechado. Toda rota técnica sem fontes é rejeitada deterministicamente.

O guardrail de saída remove PII e padrões de credencial, bloqueia frases operacionais inseguras, impede resposta técnica sem fonte e preserva as referências retornadas pela aplicação. O orquestrador recebe apenas conteúdo aprovado ou corrigido e não recebe autorização para adicionar fatos.
