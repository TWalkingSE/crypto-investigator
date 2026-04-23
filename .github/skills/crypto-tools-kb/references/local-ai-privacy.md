# IA Local e Privacidade na Investigação (Local AI)

O uso de IA baseada em nuvem (OpenAI, Anthropic) para analisar dumps de transações, listas de endereços ou históricos de chat pode violar políticas de sigilo da investigação e expor PII (Personally Identifiable Information).

## Soluções Locais (Offline)
- **Ollama:** Permite rodar modelos LLM (Llama 3, Mistral) inteiramente offline no computador do investigador. Ideal para processar grandes listas de endereços e extrair padrões.
- **LM Studio / GPT4All:** Interfaces gráficas fáceis de instalar para rodar modelos locais sem configuração complexa.
- **Any-Sync / Local RAG:** Ferramentas de RAG (Retrieval-Augmented Generation) locais para fazer perguntas aos autos do processo sem vazar dados para a internet.

## Boas Práticas
1. Anonimize ou pseudonimize os endereços `0x...` e transações antes de jogar em LLMs de nuvem, se o uso local não for possível.
2. Não faça upload de sentenças não públicas, quebras de sigilo bancário ou relatórios confidenciais (ex: RIF do COAF) para serviços web de IA.
