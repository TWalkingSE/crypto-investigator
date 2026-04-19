# DEX Analytics, DeFi e Monitoramento de Tokens

Ferramentas para analisar atividade em exchanges descentralizadas, pools de liquidez, protocolos DeFi e movimentações de tokens.

## DEX Trackers em Tempo Real

| Ferramenta | Chains | URL | Especialidade |
|---|---|---|---|
| DexScreener | 40+ chains | dexscreener.com | Preço + pool + holders + histórico |
| DEXTools | Multi-chain | dextools.io | Histórico de swaps, top traders |
| GeckoTerminal | Multi-chain | geckoterminal.com | Pools e liquidez por CoinGecko |
| Birdeye | Solana + BNB + Ethereum | birdeye.so | Excelente para Solana |
| Photon | Solana + EVM | photon-sol.tinyastro.io | Trading analytics |
| Dexscreener Multi-Chart | Multi-chain | dexscreener.com | Múltiplos pares simultâneos |

## Agregadores DEX (para rastrear swaps)

| Agregador | Chains | URL |
|---|---|---|
| 1inch | Multi-chain EVM | 1inch.io |
| Paraswap | Multi-chain EVM | paraswap.io |
| 0x / Matcha | Multi-chain EVM | matcha.xyz |
| Jupiter | Solana | jup.ag |
| CowSwap | Ethereum, Gnosis, Arbitrum | swap.cow.fi |
| Kyberswap | Multi-chain | kyberswap.com |
| LiFi | Cross-chain aggregator | li.fi |

## Pools Específicos

| DEX | Chain principal | Explorer/Analytics |
|---|---|---|
| Uniswap (V2/V3/V4) | Ethereum + L2s + Polygon | info.uniswap.org, revert.finance |
| PancakeSwap | BSC | pancakeswap.finance/info |
| SushiSwap | Multi-chain | sushi.com/analytics |
| Curve | Ethereum + L2s | curve.fi |
| Balancer | Ethereum, Arbitrum, Polygon | balancer.fi |
| Raydium | Solana | raydium.io |
| Orca | Solana | orca.so |
| SunSwap | Tron | sunswap.com |
| Trader Joe | Avalanche, Arbitrum | lfj.gg |

## DeFi Analytics (Geral)

| Ferramenta | O que faz | URL |
|---|---|---|
| DefiLlama | TVL por protocolo/chain, rendimentos | defillama.com |
| Token Terminal | Métricas fundamentalistas | tokenterminal.com |
| Dune Analytics | Dashboards SQL customizados | dune.com |
| Flipside Crypto | Dashboards comunitários | flipsidecrypto.xyz |
| Messari | Reports + analytics | messari.io |
| The Block | Data research | theblock.co/data |
| CoinDesk Data | Research institucional | coindesk.com/data |

## Monitoramento de Grandes Movimentações

| Ferramenta | O que faz | URL |
|---|---|---|
| Whale Alert | Alertas de grandes TX (Twitter + site) | whale-alert.io |
| Arkham Intel | Alertas customizáveis por entidade | arkham.com |
| Nansen Alerts | Alerts profissionais | nansen.ai |
| Etherscan Custom Alerts | Alerts por endereço | etherscan.io (grátis com conta) |
| Lookonchain | Twitter de análise on-chain | twitter.com/lookonchain |

## Lending e Borrow

| Protocolo | Chain | Explorer |
|---|---|---|
| Aave | Multi-chain | aave.com/markets |
| Compound | Ethereum | compound.finance |
| Venus | BSC | venus.io |
| Spark | Ethereum | app.spark.fi |
| Morpho | Ethereum | morpho.org |

## Yield Farming / Vaults

| Protocolo | Chain | URL |
|---|---|---|
| Yearn Finance | Ethereum + L2s | yearn.fi |
| Beefy Finance | Multi-chain | beefy.finance |
| Convex | Ethereum | convexfinance.com |
| Pendle | Ethereum + L2s | pendle.finance |

## Derivativos e Perpetuos

| Protocolo | Chain | URL |
|---|---|---|
| GMX | Arbitrum, Avalanche | gmx.io |
| dYdX | Cosmos appchain (antes StarkEx) | dydx.exchange |
| Hyperliquid | L1 própria | hyperliquid.xyz |
| Jupiter Perps | Solana | jup.ag/perps |
| Drift | Solana | drift.trade |
| Synthetix | Optimism | synthetix.io |

## Por que isso importa investigativamente

DeFi é o principal vetor de ofuscação moderno porque:

1. **Swaps em DEX**: convertem ativos rastreáveis em outros
2. **Bridges + DEXs em cascata**: multiplicam complexidade
3. **LP tokens**: fundos ficam "estacionados" em pools
4. **Lending**: depositar colateral e sacar outro ativo mascara origem
5. **Flash loans**: operações complexas em bloco único
6. **Agregadores**: roteiam swap por múltiplas DEXs dificultando análise

Ao rastrear um alvo que interagiu com DeFi, **decodifique cada TX** no Phalcon ou Tenderly para ver o fluxo real interno.
