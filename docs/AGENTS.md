# Agentes

O fluxo usa LangChain `create_agent` para seis papéis, coordenados por LangGraph:

1. `roteador`: classifica intenção e não responde tecnicamente;
2. `ativos_solares`: usa RAG para componentes, eficiência e ambiente;
3. `manutencao`: orienta sobre manutenção e relatórios, sem registrar operações;
4. `seguranca`: recusa práticas inseguras e reforça controles aplicáveis;
5. `faq_apolloai`: explica identidade, escopo e limitações;
6. `juiz_factual`: avalia o rascunho do especialista e aprova, corrige ou rejeita a resposta.

O caminho técnico é guardrail de entrada → roteador → especialista → juiz factual → guardrail de saída. Uma solicitação chama apenas o especialista selecionado. O classificador de entrada não faz parte dos seis papéis.

Bloqueios de entrada encerram o fluxo antes do roteador. Interações sociais reconhecidas recebem uma resposta direta. Solicitações classificadas pelo roteador como fora do escopo terminam sem chamar especialista. Respostas técnicas passam pelo juiz, que exige fontes recuperadas para aprová-las.
