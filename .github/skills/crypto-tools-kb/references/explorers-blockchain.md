# Explorers de Blockchain — Referência Completa

Explorers são a ferramenta básica do investigador on-chain. Cada blockchain tem explorer(s) dedicado(s) e, quando há múltiplas opções, escolha o mais completo para a sua análise.

## Multi-Chain (busca universal)

| Ferramenta | Chains suportadas | URL | Nota |
|---|---|---|---|
| Blockchair | 35+ blockchains | blockchair.com | Melhor ferramenta multi-chain gratuita; exporta CSV |
| Blockscan (Etherscan) | Ethereum + L2s + sidechains | blockscan.com | Busca única em todos os sites "scan" |
| Chainlist | Metadados de redes EVM | chainlist.org | Chain ID, RPCs, currency symbol |
| OKLink | 40+ blockchains | oklink.com | Análise de tokens e DeFi agregada |
| DefiLlama | DeFi multi-chain | defillama.com | TVL, protocolos, chain overview |

## Bitcoin (UTXO)

| Ferramenta | URL | Especialidade |
|---|---|---|
| Mempool.space | mempool.space | Tempo real, análise de fees, mempool viewer |
| Blockchain.com Explorer | blockchain.com/explorer | Explorer clássico |
| Blockstream | blockstream.info | Explorer minimalista, suporta Liquid |
| Blockchair | blockchair.com/bitcoin | Filtros avançados, exportação |
| BTC.com | explorer.btc.com | Pool stats, block details |
| OXT.me | oxt.me | Análise de grafos, co-spending, change detection |
| WalletExplorer | walletexplorer.com | Clusterização de endereços |
| Bitref | bitref.com | Saldo rápido |
| SoChain | sochain.com | Multi-UTXO (BTC, LTC, DOGE, DASH) |

## Litecoin, Bitcoin Cash, Dogecoin, Dash, Zcash (UTXO)

| Blockchain | Explorer principal | Alternativas |
|---|---|---|
| Litecoin | blockchair.com/litecoin | blockcypher.com/ltc, litecoinblockexplorer.net |
| Bitcoin Cash | blockchair.com/bitcoin-cash | explorer.bitcoin.com, blockchair.com/bitcoin-cash |
| Dogecoin | blockchair.com/dogecoin | dogechain.info, blockcypher.com/doge |
| Dash | blockchair.com/dash | dashblockexplorer.com, chainz.cryptoid.info/dash |
| Zcash | blockchair.com/zcash | zcashblockexplorer.com, zchain.info |

## Ethereum e L2s (EVM)

| Rede | Chain ID | Explorer oficial | Alternativas |
|---|---|---|---|
| Ethereum | 1 | etherscan.io | ethplorer.io, beaconcha.in (consensus layer) |
| Arbitrum One | 42161 | arbiscan.io | explorer.arbitrum.io |
| Optimism | 10 | optimistic.etherscan.io | optimism.io/explorer |
| Base | 8453 | basescan.org | explorer.base.org |
| zkSync Era | 324 | explorer.zksync.io | era.zksync.network |
| Linea | 59144 | lineascan.build | explorer.linea.build |
| Scroll | 534352 | scrollscan.com | scroll.io |
| Starknet | — | starkscan.co | voyager.online |

## Outras EVMs

| Rede | Chain ID | Explorer |
|---|---|---|
| BNB Smart Chain | 56 | bscscan.com |
| Polygon PoS | 137 | polygonscan.com |
| Polygon zkEVM | 1101 | zkevm.polygonscan.com |
| Avalanche C-Chain | 43114 | snowtrace.io |
| Fantom | 250 | ftmscan.com |
| Cronos | 25 | cronoscan.com |
| Gnosis Chain | 100 | gnosisscan.io |
| Celo | 42220 | celoscan.io |
| Moonbeam | 1284 | moonbeam.moonscan.io |
| Harmony | 1666600000 | explorer.harmony.one |
| Kava EVM | 2222 | kavascan.com |
| Metis | 1088 | andromeda-explorer.metis.io |
| Boba | 288 | bobascan.com |
| Mantle | 5000 | explorer.mantle.xyz |

## Non-EVM

| Blockchain | Explorer principal | Alternativas |
|---|---|---|
| Solana | solscan.io | explorer.solana.com, solanabeach.io, solanafm.com |
| Tron | tronscan.org | trongrid.io |
| Ripple (XRP) | xrpscan.com | bithomp.com, livenet.xrpl.org |
| Cardano | cardanoscan.io | explorer.cardano.org, pool.pm |
| Cosmos Hub | mintscan.io | atomscan.com |
| Polkadot | subscan.io | polkadot.js.org/apps |
| TON | tonscan.org | tonscan.com, dton.io |
| Algorand | allo.info | algoexplorer.io (descontinuado — usar Allo) |
| Near | explorer.near.org | nearblocks.io |
| Stellar | stellarchain.io | steexp.com |
| EOS | bloks.io | eosauthority.com |
| Tezos | tzkt.io | tezblock.io |
| Hedera | hashscan.io | hederaexplorer.io |
| Aptos | aptoscan.com | explorer.aptoslabs.com |
| Sui | suiscan.xyz | explorer.sui.io |

## Privacy Coins

| Blockchain | Explorer | Limitação |
|---|---|---|
| Monero | xmrchain.net, localmonero.co/blocks | Não mostra senders nem receivers (ring signatures) |
| Zcash shielded | — | Pools shielded não têm explorer público |
| Dash PrivateSend | blockchair.com/dash | Agregações de CoinJoin parcialmente visíveis |

## Dicas de Uso

- Ao investigar um endereço `0x`, sempre verifique em **múltiplas redes EVM** (mesmo endereço, saldos diferentes)
- Para Bitcoin, sempre cruze com **WalletExplorer** para identificar clusters conhecidos
- Para tokens, verifique o contrato oficial antes de analisar — tokens com nomes similares podem ser scam copies
- Explorers podem ter **labels públicos** (nome da exchange, protocolo DeFi, etc.) — sempre verificar
- Alguns explorers têm **API pública** para automação (Etherscan, Blockchair, etc.)
