# RAG solar

`SolarKnowledgeBase` lê os Markdown durante a indexação. O conversor usa `pypdf` para extrair o texto de cada página dos PDFs originais. O texto é normalizado, dividido em chunks com sobreposição e transformado em vetores por signed feature hashing no indexador. Os vetores e metadados são enviados ao Qdrant remoto. A busca no Qdrant aplica um filtro lexical para reduzir colisões; uma expansão determinística de termos técnicos em português para equivalentes em inglês ajuda a consultar as publicações IEA PVPS sem alterar os documentos originais.

`python -m scripts.convert_pdfs_to_markdown` gera 19 arquivos em `data/solar/documentos/markdown/`, mantendo o texto separado por página. O indexador exige uma cópia Markdown para cada PDF e conserva o nome e a página do PDF na fonte. O comando não usa API de IA. Tabelas, imagens e texto com mapeamento de caracteres defeituoso podem exigir revisão manual; o texto não é resumido nem traduzido.

Para indexar no Qdrant, configure `QDRANT_URL` e `QDRANT_API_KEY` e execute `python -m scripts.index_qdrant`. O comando lê diretamente os Markdown atuais, gera os vetores de hashing localmente e usa as coleções `rag_chunks` e `memoria_resumos`. Ele exige um Markdown para cada PDF antes de criar as coleções e recusa indexar sobre coleções não vazias; a exclusão remota fica a cargo do operador. Transformar PDF em Markdown, por si só, não remove a necessidade de calcular vetores para Qdrant; esse cálculo não usa Gemini.

Metadados preservados: documento, página quando disponível, seção inferida, URL original, trecho e score. Não há índice JSON local nem geração de índice durante o build da imagem. A API exige as coleções remotas; uma falha do Qdrant resulta em erro controlado, sem busca alternativa.

Os especialistas recebem somente trechos retornados pelo servidor MCP. Sem fonte acima do limiar, o juiz reprova a resposta técnica e a API informa insuficiência. A publicação e a situação do artefato atualmente indexado estão descritas em `data/solar/fontes.md`; nenhuma URL ou página é fabricada.

## Avaliação reproduzível

`python scripts/evaluate_rag.py` consulta as coleções remotas indexadas com os casos versionados em `data/solar/rag_eval.json`. O gate exige acerto em todos os casos relevantes e rejeição dos casos fora do domínio. O relatório inclui hit rate, mean reciprocal rank e detalhes por pergunta. A CI executa testes unitários simulados; esta avaliação depende de credenciais e é executada separadamente.
