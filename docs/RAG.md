# RAG solar

`SolarKnowledgeBase` aceita `.pdf`, `.md` e `.txt`. Para PDFs, `pypdf` extrai cada página. O texto é normalizado, dividido em chunks com sobreposição, transformado em embeddings esparsos locais por signed feature hashing e salvo em um índice JSON gerado. A busca híbrida combina similaridade vetorial e cobertura lexical; a interseção obrigatória reduz colisões e respostas irrelevantes. Uma expansão determinística de termos técnicos em português para equivalentes em inglês permite consultar as publicações IEA PVPS sem traduzir ou alterar os documentos originais.

Metadados preservados: documento, página quando disponível, seção inferida, URL original, trecho e score. O índice gerado não é versionado; é reproduzido com:

```bash
python scripts/index_knowledge.py
```

A imagem Docker gera o índice durante o build para que a primeira consulta não pague o custo de extração de todas as páginas.

Os especialistas recebem somente trechos retornados pelo servidor MCP. Sem fonte acima do limiar, o juiz reprova a resposta técnica e a API informa insuficiência. A publicação e a situação do artefato atualmente indexado estão descritas em `data/solar/fontes.md`; nenhuma URL ou página é fabricada.

## Avaliação reproduzível

`python scripts/evaluate_rag.py` executa os casos versionados em `data/solar/rag_eval.json`, incluindo manutenção NREL e temas IEA PVPS como degradação, PV flutuante, KPIs, agrivoltaicos e PV+BESS. O gate exige acerto em todos os casos relevantes e rejeição de todos os casos deliberadamente fora do domínio. O relatório inclui hit rate, mean reciprocal rank e detalhes por pergunta; a CI falha se o piso deixar de ser atendido.
