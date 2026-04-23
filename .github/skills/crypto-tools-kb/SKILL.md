---
name: crypto-tools-kb
description: >
  Base de conhecimento de ferramentas OSINT e forenses para investigação em 
  criptoativos. CONSULTE SEMPRE antes de recomendar qualquer ferramenta. 
  Contém catálogo organizado por categoria: explorers (multi-chain e 
  específicos), análise de carteiras e entidades, rastreamento forense 
  institucional, visualização de fluxo, análise de contratos, detecção de 
  scam, NFT, DeFi analytics, CLI/open-source, bases de endereços maliciosos, 
  e ferramentas brasileiras. Use quando o investigador perguntar "qual 
  ferramenta usar para X" ou precisar de opções além das já mencionadas.
---

# Base de Conhecimento — Ferramentas de Investigação Forense

## Como Usar

Consulte o arquivo de referência adequado ao tema. Cada arquivo contém tabelas com nome, função, URL, custo (gratuito/pago/licença) e particularidades.

## Índice de Referências

| Tema da necessidade | Arquivo em `references/` |
|---|---|
| Explorers e visualização básica de blockchains | `explorers-blockchain.md` |
| Análise de carteiras, entidades, labels e clusters | `analise-carteiras.md` |
| Rastreamento forense (Chainalysis, TRM, Elliptic, etc.) | `forense-institucional.md` |
| Visualização de fluxo e grafos de transações | `visualizacao-fluxo.md` |
| Análise de smart contracts e detecção de scam | `contratos-e-scam.md` |
| DEX analytics, DeFi e monitoramento de tokens | `dex-defi.md` |
| NFT marketplaces e análise | `nft.md` |
| Ferramentas CLI e open-source | `cli-open-source.md` |
| Bases de endereços maliciosos e sanções | `bases-maliciosos.md` |
| Ferramentas e fontes brasileiras | `brasil.md` |
| IA Local e Privacidade na Investigação | `local-ai-privacy.md` |

## Regras de Uso

- **Sempre** indique custo da ferramenta (gratuita / pago / licença institucional)
- **Sempre** indique limitações conhecidas
- **Nunca** recomende ferramenta sem verificar se cobre a blockchain em análise
- **Prefira** ferramentas gratuitas e open-source quando o caso permitir
- Para casos com implicação processual, recomendar ferramentas **institucionais auditadas** (Chainalysis, TRM, Elliptic)
- Para triagem inicial, ferramentas gratuitas (Etherscan, DeBank, Arkham) são suficientes

## Ferramentas Essenciais (top 20 para começar)

Se o investigador pedir "por onde começo?", estas são as essenciais:

| Ferramenta | Categoria | URL | Custo |
|---|---|---|---|
| Etherscan | Explorer Ethereum | etherscan.io | Gratuito |
| BscScan | Explorer BSC | bscscan.com | Gratuito |
| Blockchair | Multi-chain | blockchair.com | Gratuito |
| Mempool.space | Bitcoin tempo real | mempool.space | Gratuito |
| WalletExplorer | Clusters Bitcoin | walletexplorer.com | Gratuito |
| OXT.me | Grafo Bitcoin | oxt.me | Gratuito |
| DeBank | Portfolio multi-chain EVM | debank.com | Gratuito |
| Arkham Intelligence | Entidades + labels | platform.arkham.intelligence | Freemium |
| Tronscan | Explorer Tron | tronscan.org | Gratuito |
| Solscan | Explorer Solana | solscan.io | Gratuito |
| Breadcrumbs | Visualização fluxo | breadcrumbs.app | Freemium |
| Metasleuth | Rastreamento visual | metasleuth.io | Freemium |
| Misttrack | Fundos roubados | misttrack.io | Freemium |
| Token Sniffer | Detecção scam token | tokensniffer.com | Gratuito |
| Honeypot.is | Detecção honeypot | honeypot.is | Gratuito |
| Revoke.cash | Verificar/revogar approvals | revoke.cash | Gratuito |
| DexScreener | DEX tempo real | dexscreener.com | Gratuito |
| Chainabuse | Denúncias fraude | chainabuse.com | Gratuito |
| Bubblemaps | Clusters visuais | bubblemaps.io | Freemium |
| OFAC SDN List | Sanções EUA | home.treasury.gov | Gratuito |

Para catálogo completo (100+ ferramentas), consulte os arquivos de referência.
