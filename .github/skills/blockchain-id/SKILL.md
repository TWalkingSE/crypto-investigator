---
name: blockchain-id
description: >
  Protocolo obrigatório de identificação de blockchain para endereços começando 
  com 0x. Use SEMPRE que o usuário fornecer um endereço 0x sem indicar qual 
  rede (Ethereum, BSC, Polygon, Arbitrum, etc.). Também use quando houver 
  dúvida sobre em qual blockchain investigar um endereço, hash ou transação. 
  Endereços 0x existem simultaneamente em dezenas de redes EVM com 
  transações completamente diferentes em cada uma — erro investigativo 
  fatal é assumir que é Ethereum sem verificar.
---

# Protocolo de Identificação de Blockchain

## Por que isso importa

Todas as blockchains compatíveis com EVM (Ethereum Virtual Machine) usam o mesmo formato de endereço: `0x` + 40 caracteres hexadecimais. O endereço `0xABC...123` pode existir **simultaneamente** em Ethereum, BSC, Polygon, Arbitrum, Avalanche, Base, Optimism, e dezenas de outras redes — com saldos, transações e tokens **completamente diferentes** em cada uma.

**Erro investigativo fatal:** Assumir que um endereço 0x é Ethereum sem verificar. Você pode estar rastreando a rede errada.

## Protocolo Obrigatório

Sempre que o usuário fornecer um endereço começando com `0x`, execute este protocolo ANTES de qualquer análise.

### PASSO 1 — Pergunte (se não informado)

> "Este endereço começa com 0x, o que significa que pode existir em qualquer blockchain compatível com EVM (Ethereum, BSC, Polygon, Arbitrum, etc.). Em qual blockchain você está investigando este endereço? Se não souber, me diga de onde obteve o endereço (qual exchange, qual relatório, qual investigação) para ajudar a determinar."

### PASSO 2 — Verificação multi-chain (se usuário não souber)

Oriente o investigador a usar uma das ferramentas de varredura multi-chain:

| Ferramenta | O que faz | URL |
|---|---|---|
| **DeBank** | Mostra saldo em TODAS as chains EVM de um endereço 0x | debank.com |
| **Arkham Intelligence** | Portfolio multi-chain + entidades identificadas | platform.arkham.intelligence |
| **Zapper** | Dashboard multi-chain de carteira | zapper.xyz |
| **Blockchair** | Explorer multi-chain com busca universal | blockchair.com |
| **Nansen Portfolio** | Análise multi-chain de carteira | nansen.ai |

Instrução padrão:
> "Acesse debank.com, cole o endereço 0x na barra de busca. O DeBank vai mostrar o saldo desse endereço em TODAS as redes EVM e revelar em quais blockchains tem atividade. Me envie o resultado (captura de tela ou lista) para direcionar a análise."

### PASSO 3 — Use o explorer correto

Uma vez identificada a rede, use o explorer específico. **NUNCA analise dados de uma rede como se fossem de outra.**

| Blockchain | Chain ID | Explorer principal |
|---|---|---|
| Ethereum | 1 | etherscan.io |
| BNB Smart Chain (BSC) | 56 | bscscan.com |
| Polygon (PoS) | 137 | polygonscan.com |
| Avalanche C-Chain | 43114 | snowtrace.io |
| Arbitrum One | 42161 | arbiscan.io |
| Optimism | 10 | optimistic.etherscan.io |
| Base | 8453 | basescan.org |
| Fantom | 250 | ftmscan.com |
| Cronos | 25 | cronoscan.com |
| Gnosis (xDai) | 100 | gnosisscan.io |
| zkSync Era | 324 | explorer.zksync.io |
| Linea | 59144 | lineascan.build |
| Celo | 42220 | celoscan.io |

## Identificação por Contexto

Se o endereço vier de uma fonte conhecida, use essas pistas:

| Fonte do endereço | Blockchain provável |
|---|---|
| Etherscan | Ethereum |
| BscScan | BSC |
| Polygonscan | Polygon |
| Arbiscan | Arbitrum |
| Relatório de exchange mencionando "rede BEP-20" ou "BSC" | BSC |
| Relatório mencionando "rede ERC-20" | Ethereum |
| Relatório mencionando "rede TRC-20" | Tron (endereço T... — não 0x) |
| Hash de transação (0x + 64 caracteres) | Verificar em qual explorer o hash retorna resultado |

## Endereços NÃO-EVM (não começam com 0x)

Se o endereço não começa com 0x, identifique pelo formato:

| Prefixo/Formato | Blockchain | Explorer |
|---|---|---|
| `1...`, `3...`, `bc1q...`, `bc1p...` | Bitcoin | blockchair.com, mempool.space |
| `L...`, `M...`, `ltc1q...` | Litecoin | blockchair.com/litecoin |
| `bitcoincash:q...` | Bitcoin Cash | blockchair.com/bitcoin-cash |
| `D...` | Dogecoin | blockchair.com/dogecoin |
| `t1...`, `zs1...` | Zcash (transparente / shielded) | blockchair.com/zcash |
| `X...` | Dash | blockchair.com/dash |
| `T...` (Base58Check) | Tron | tronscan.org |
| `r...` | Ripple (XRP) | xrpscan.com |
| `addr1...` | Cardano | cardanoscan.io |
| `cosmos1...` | Cosmos | mintscan.io |
| `EQ...`, `UQ...` | TON | tonscan.org |
| Base58 32-44 chars (So1..., 7xK...) | Solana | solscan.io |
| `fulano.near` ou hash | Near | explorer.near.org |

## Investigação Multi-Chain (Vantagem Investigativa)

Em investigações reais, o mesmo indivíduo frequentemente usa o MESMO endereço 0x em múltiplas redes EVM (porque a chave privada é a mesma). Isso é uma **vantagem investigativa**: atividade em BSC pode complementar o que se vê em Ethereum, e vice-versa.

**Instrução ao investigador:** quando o alvo usar endereço EVM, verificar TODAS as redes relevantes — não apenas a primeira identificada.

## Após identificar a blockchain

Direcione para o skill de rastreamento apropriado:
- UTXO (Bitcoin, Litecoin, Dogecoin, etc.) → use `/utxo-tracing`
- Account-based EVM (Ethereum, BSC, etc.) → use `/account-tracing`
- Account-based não-EVM (Solana, Tron, etc.) → use `/account-tracing` com adaptações
- Multi-hop / cross-chain → use `/cross-chain-tracing`
