# Análise de Carteiras, Entidades e Labels

Ferramentas para identificar: quem é o dono de um endereço, em quais redes tem atividade, qual o comportamento típico e quais relações tem com outros endereços.

## Portfolio Multi-Chain

| Ferramenta | Especialidade | URL | Custo |
|---|---|---|---|
| DeBank | Portfolio + labels multi-chain EVM | debank.com | Gratuito |
| Zapper | Dashboard DeFi + NFT | zapper.xyz | Gratuito |
| Zerion | Portfolio + tracking | zerion.io | Gratuito |
| Nansen Portfolio | Análise profissional | nansen.ai | Pago |
| Step Finance | Portfolio Solana | step.finance | Gratuito |

## Entidades e Labels (identificação de dono)

| Ferramenta | O que faz | URL | Custo |
|---|---|---|---|
| Arkham Intelligence | Deanonimização, entidades, multi-chain | platform.arkham.intelligence | Freemium |
| Etherscan Labels | Labels públicos Ethereum | etherscan.io/labelcloud | Gratuito |
| BscScan Labels | Labels públicos BSC | bscscan.com/labelcloud | Gratuito |
| Nansen | Smart money, labels profissionais | nansen.ai | Pago |
| Breadcrumbs | Entidades + relações | breadcrumbs.app | Freemium |
| WalletExplorer | Clusters Bitcoin (exchanges conhecidas) | walletexplorer.com | Gratuito |
| BitInfoCharts | Rich list, labels BTC/ETH/DOGE | bitinfocharts.com | Gratuito |

## Clusterização e Relações

| Ferramenta | O que faz | URL | Custo |
|---|---|---|---|
| Bubblemaps | Visualiza clusters e conexões entre holders | bubblemaps.io | Freemium |
| Nansen Wallet Profiler | Classificação comportamental | nansen.ai | Pago |
| GraphSense | Análise acadêmica de grafos | graphsense.info | Open-source |
| Crystal Blockchain | Análise institucional | crystalblockchain.com | Licença |
| Arkham Ultra | Inteligência profunda | arkham.com | Pago |

## Análise Comportamental

| Ferramenta | O que faz | URL |
|---|---|---|
| DexScreener | Comportamento de carteira em DEXs | dexscreener.com |
| DEXTools | Top traders, histórico por carteira | dextools.io |
| Cielo | Tracking de carteiras (wallet following) | cielo.finance |
| Zerion Wallets | Portfolio + histórico | zerion.io |
| ApeBoard | Multi-chain portfolio | apeboard.finance |

## Ripple (XRP) — Caso Especial

Como XRP usa **destination tags**, ferramentas específicas:

| Ferramenta | URL |
|---|---|
| Bithomp | bithomp.com (identifica exchanges por tag) |
| XRPScan | xrpscan.com |

## Near — Nomes Legíveis

Near usa nomes como `fulano.near` — ferramentas:

| Ferramenta | URL |
|---|---|
| Near Explorer | explorer.near.org |
| NearBlocks | nearblocks.io (inclui busca por nome) |

## Uso Típico em Investigação

1. **Triagem inicial:** DeBank + Arkham para ver saldo multi-chain e labels
2. **Clusterização:** Bubblemaps para ver conexões; WalletExplorer para Bitcoin
3. **Deep dive:** Nansen ou Arkham Ultra para análise profissional
4. **Grafos:** GraphSense ou Breadcrumbs para visualização

## Como Verificar Se um Endereço é de Exchange

1. Buscar label no Etherscan/BscScan/etc. (aba Overview)
2. Buscar em Arkham (categoria "CEX")
3. Verificar em WalletExplorer para Bitcoin
4. Analisar padrão: alto volume + muitas counterparts + transações regulares 24/7 = provável hot wallet de exchange
5. Cruzar com base de dados pública de endereços de exchanges (chainalysis.com/blog)
