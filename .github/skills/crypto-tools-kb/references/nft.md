# NFT — Marketplaces e Análise

NFTs (ERC-721, ERC-1155) podem ser instrumentos de lavagem (wash trading), veículos de transferência patrimonial e parte de esquemas fraudulentos.

## Marketplaces Principais

| Marketplace | Chains | URL | Nota |
|---|---|---|---|
| OpenSea | Ethereum, Polygon, Arbitrum, Optimism, Base, Solana | opensea.io | Maior marketplace global |
| Blur | Ethereum | blur.io | Alta liquidez em blue-chips |
| Magic Eden | Solana, Ethereum, Polygon, Bitcoin Ordinals | magiceden.io | Líder em Solana |
| LooksRare | Ethereum | looksrare.org | — |
| X2Y2 | Ethereum | x2y2.io | — |
| Tensor | Solana | tensor.trade | Pro traders |
| Rarible | Multi-chain | rarible.com | — |
| Foundation | Ethereum | foundation.app | Arte curatorial |
| SuperRare | Ethereum | superrare.com | Arte 1/1 |
| MintSquare | zkSync, Starknet | mintsquare.io | L2s |
| OrdinalsBot | Bitcoin Ordinals | ordinalsbot.com | Inscrições Bitcoin |

## Exploradores e Analytics

| Ferramenta | O que faz | URL |
|---|---|---|
| NFTScan | Multi-chain NFT explorer | nftscan.com |
| Reservoir | API + marketplace aggregator | reservoir.tools |
| Moby | NFT analytics | moby.gg |
| NFT Price Floor | Histórico de floor | nftpricefloor.com |
| DappRadar (NFT) | Volume por coleção | dappradar.com/nft |
| CryptoSlam | Rankings de NFT | cryptoslam.io |

## Análise de Wash Trading

Wash trading em NFT ocorre quando o mesmo dono compra e vende repetidamente para inflar volume:

| Ferramenta | O que detecta | URL |
|---|---|---|
| NFTGo | Detecção de wash trading | nftgo.io |
| Chainalysis Reports | Relatórios periódicos sobre wash trading | chainalysis.com/reports |
| Cryptoslam (Filtered) | Volume filtrado excluindo wash trading | cryptoslam.io |
| Dune (Dashboards comunitários) | Queries SQL para detectar wash | dune.com |

**Indicadores de wash trading:**
- Compra e venda entre endereços com mesma fonte de gás
- Preços muito acima/abaixo do floor sem justificativa
- Volume alto em coleção com pouca atividade real
- Endereços com histórico de TX apenas com a coleção em análise
- Timing suspeito (minutos entre compra e venda)

## Análise de Coleção

Para investigar uma coleção NFT específica:

1. **OpenSea**: veja histórico de transferências, top holders, volume
2. **NFTScan**: dados multi-chain, deploy info, creator
3. **Etherscan (contrato)**: código da coleção, owner, supply
4. **Bubblemaps**: clusters de holders
5. **Dune**: dashboards específicos da coleção

## NFT como Veículo de Lavagem

Padrões investigativos:

- **Auto-compra inflacionada**: NFT comprado por R$1M entre endereços do mesmo controlador, depois vendido legitimamente por R$200k — "limpou" R$800k
- **Transferência patrimonial sem fiat**: NFT de alto valor enviado de A para B sem venda (gift) — transfere patrimônio
- **Royalties como canal**: criador recebe royalty a cada venda — pode ser usado para canalizar fundos

## Bitcoin Ordinals e Inscrições

Novas formas de NFT em Bitcoin (desde 2023):

| Ferramenta | URL |
|---|---|
| Ordinals.com | ordinals.com (dados oficiais) |
| Magic Eden Ordinals | magiceden.io/ordinals |
| Unisat | unisat.io |
| OrdinalHub | ordinalhub.com |

Inscrições são dados armazenados em Bitcoin via Taproot — análise é parcialmente diferente de NFTs ERC-721.

## Como Investigar Suspeita de Wash Trading

1. Identifique a coleção e período suspeito
2. Liste todas as TX de venda com valor acima de 2x o floor
3. Para cada TX suspeita:
   - Verifique o comprador e vendedor
   - Analise fonte de gás (mesmo endereço fundando ambos?)
   - Verifique se os endereços têm outras TX normais
4. Use NFTGo ou Dune para cruzar com métricas
5. Documente o padrão (compras/vendas cíclicas entre mesmo grupo)
