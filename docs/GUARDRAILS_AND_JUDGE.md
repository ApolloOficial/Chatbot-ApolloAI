# Guardrails e juiz factual

O guardrail de entrada aplica verificações baratas primeiro: prompt injection, acesso a dados internos, ofensa, prática perigosa e temas explicitamente fora do escopo. Em mensagens restantes, o modelo faz classificação semântica. Saudações, agradecimentos e perguntas legítimas de segurança são permitidos. Bloqueios terminam sem especialistas.

O juiz recebe rascunho e exatamente as fontes recuperadas. Sua decisão Pydantic contém aprovação/correção/rejeição, fundamentação, segurança, escopo, validade das fontes, possível hipótese tratada como diagnóstico, motivos e eventual resposta corrigida. Decisão inválida falha de modo fechado. Toda rota técnica sem fontes é rejeitada deterministicamente.

O guardrail de saída remove PII e padrões de credencial, bloqueia frases operacionais inseguras, impede resposta técnica sem fonte e preserva as referências retornadas pela aplicação. O orquestrador recebe apenas conteúdo aprovado ou corrigido e não recebe autorização para adicionar fatos.
