# Arquitetura do ApolloAI

```mermaid
flowchart LR
    Mobile[Aplicativo Apollo] -->|POST /chat + contexto informado| Flask[Flask / Blueprints]
    External[Agente externo] -->|A2A 1.0 / SendMessage| Flask
    Flask --> GE[Guardrail de entrada]
    GE --> R[Roteador LangChain]
    R --> A[Especialista em ativos]
    R --> M[Especialista em manutenção]
    R --> S[Especialista em segurança]
    R --> F[FAQ ApolloAI]
    A & M & S --> MC[Cliente MCP]
    MC --> MS[Servidor MCP stdio]
    MS --> RAG[Índice vetorial solar]
    A & M & S & F --> J[Juiz factual]
    J --> O[Orquestrador]
    O --> GS[Guardrail de saída]
    Flask <--> Mongo[(MongoDB: sessões e observabilidade)]
    Flask -. cache / ranking .-> Redis[(Redis opcional)]
    Flask --> Prom[/Métricas Prometheus/]
```

O backend Spring e o PostgreSQL operacional do Apollo estão fora desta fronteira. O ApolloAI recebe apenas contexto já fornecido pelo aplicativo ou pelo técnico. Não identifica, ativa ou altera placas e não registra manutenção.

O padrão Application Factory separa configuração e construção da aplicação. Blueprints separam os contratos HTTP e A2A; Repository encapsula MongoDB; Adapter conecta o grafo ao MCP; StateGraph explicita a orquestração. O estado durável não depende do processo Flask nem do checkpointer em memória.
