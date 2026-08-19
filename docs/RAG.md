# RAG solar

`SolarKnowledgeBase` aceita `.pdf`, `.md` e `.txt`. Para PDFs, `pypdf` extrai cada página. O texto é normalizado, dividido em chunks com sobreposição, transformado em embeddings locais por signed feature hashing e salvo em um índice JSON gerado. A busca usa similaridade de cosseno e interseção lexical mínima para reduzir colisões e respostas irrelevantes.

Metadados preservados: documento, página quando disponível, seção inferida, URL original, trecho e score. O índice gerado não é versionado; é reproduzido com:

```bash
python scripts/index_knowledge.py
```

Os especialistas recebem somente trechos retornados pelo servidor MCP. Sem fonte acima do limiar, o juiz reprova a resposta técnica e a API informa insuficiência. A publicação e a situação do artefato atualmente indexado estão descritas em `data/solar/fontes.md`; nenhuma URL ou página é fabricada.
