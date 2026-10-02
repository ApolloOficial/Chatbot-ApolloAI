# RAG solar

`SolarKnowledgeBase` lê os Markdown durante a indexação. O conversor usa `pypdf` para extrair o texto de cada página dos PDFs originais. O texto é normalizado, dividido em trechos de até 350 caracteres com sobreposição e transformado pelo modelo multilíngue `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` usando FastEmbed/ONNX em CPU. Cada vetor tem 384 dimensões. O mesmo modelo gera os vetores de documentos, perguntas e resumos de memória; a consulta é vetorizada uma vez no processo Flask e enviada ao servidor MCP junto com o texto, evitando carregar o modelo no subprocesso MCP de cada consulta.

A busca usa similaridade cosseno no Qdrant sem exigir palavras iguais entre a pergunta e o trecho, o que permite consultas em português sobre fontes em inglês e paráfrases. `RAG_MIN_SCORE` define o limiar mínimo de relevância (padrão `0.35`); resultados abaixo dele são descartados e o juiz mantém a recusa quando não há evidência suficiente. A qualidade deve ser confirmada pelo dataset de avaliação versionado, incluindo consultas cruzadas entre português e inglês e perguntas fora do domínio; o uso de embeddings não garante por si só que uma resposta esteja correta.

`python -m scripts.convert_pdfs_to_markdown` gera 19 arquivos em `data/solar/documentos/markdown/`, mantendo o texto separado por página. O indexador exige uma cópia Markdown para cada PDF e conserva o nome e a página do PDF na fonte. O comando não usa API de IA. Tabelas, imagens e texto com mapeamento de caracteres defeituoso podem exigir revisão manual; o texto não é resumido nem traduzido.

Para indexar no Qdrant, configure `QDRANT_URL`, `QDRANT_API_KEY` e `MONGODB_URI`, então execute `python -m scripts.index_qdrant`. Na primeira execução, o FastEmbed baixa o modelo para `FASTEMBED_CACHE_DIR`; as execuções seguintes reutilizam o cache. O indexador cria as coleções novas `rag_chunks_v2` e `memoria_resumos_v2`, exige um Markdown para cada PDF, recusa coleções v2 não vazias e reindexa os resumos persistidos no MongoDB. As coleções antigas `rag_chunks` e `memoria_resumos` permanecem intactas. Para repetir uma indexação v2, remova manualmente apenas as coleções v2 no Qdrant antes de executar o indexador; ele não apaga dados remotos.

Metadados preservados: documento, página quando disponível, seção inferida, URL original, trecho e score. Não há índice JSON local nem geração do índice de documentos durante o build da imagem. A API valida se as coleções v2 usam vetores de 384 dimensões e exige o Qdrant remoto; incompatibilidade ou falha resulta em erro controlado, sem busca alternativa.

Os especialistas recebem somente trechos retornados pelo servidor MCP. Sem fonte acima do limiar, o juiz reprova a resposta técnica e a API informa insuficiência. A publicação e a situação do artefato atualmente indexado estão descritas em `data/solar/fontes.md`; nenhuma URL ou página é fabricada.

## Avaliação reproduzível

`python scripts/evaluate_rag.py` consulta as coleções remotas indexadas com os casos versionados em `data/solar/rag_eval.json`. O gate exige acerto em todos os casos relevantes e rejeição dos casos fora do domínio. O relatório inclui hit rate, mean reciprocal rank, score do primeiro resultado e detalhes por pergunta. A CI executa testes unitários simulados; esta avaliação depende de credenciais e é executada separadamente.
