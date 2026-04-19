---
name: account-tracing
description: >
  Rastreamento forense em blockchains account-based — Ethereum, BSC, Polygon, 
  Arbitrum, Optimism, Base, Avalanche, Solana, Tron, Ripple, Cosmos, Polkadot, 
  TON, Algorand, Near. Use para análise de endereços, transações, tokens ERC-20, 
  BEP-20, SPL, TRC-20, internal transactions, token transfers, aprovações 
  (allowances), eventos de contrato, NFTs (ERC-721, ERC-1155). Inclui técnicas 
  específicas para Etherscan e explorers similares, interpretação de traces, 
  decodificação de swaps e interação com contratos.
---

# Rastreamento Account-Based — Ethereum e Similares

## Conceito Central: Account

**Como funciona:** Cada endereço é uma "conta" com saldo, como uma conta bancária. Transações debitam de uma conta e creditam outra diretamente. Não existe conceito de UTXO ou troco.

**Implicação investigativa:**
- Rastreamento é mais intuitivo: A enviou X para B, sem ambiguidade de troco
- Porém, **contratos inteligentes complicam tudo**: um único TX hash pode mover fundos por dezenas de contratos (internal transactions)
- **Token transfers** são separados da transação nativa: uma TX ETH pode não mover ETH nenhum, mas mover milhões em USDT via contrato ERC-20
- **Aprovações (allowances)**: contratos podem mover tokens SEM nova assinatura — investigar `approve()` e `transferFrom()`
- **Nonce sequencial**: cada transação tem número de sequência, permitindo ordenação precisa

## Blockchains Account-Based EVM

| Blockchain | Chain ID | Explorer | Nota investigativa |
|---|---|---|---|
| **Ethereum** | 1 | etherscan.io | Maior volume DeFi e NFT |
| **BNB Smart Chain** | 56 | bscscan.com | Alto volume de tokens fraudulentos e rug pulls |
| **Polygon (PoS)** | 137 | polygonscan.com | Taxas baixas — microtransações e jogos |
| **Avalanche C-Chain** | 43114 | snowtrace.io | Subnets podem ter explorers separados |
| **Arbitrum One** | 42161 | arbiscan.io | L2 — liquida no Ethereum |
| **Optimism** | 10 | optimistic.etherscan.io | L2 do Ethereum |
| **Base** | 8453 | basescan.org | L2 da Coinbase |
| **Fantom** | 250 | ftmscan.com | DeFi |
| **Cronos** | 25 | cronoscan.com | Ecossistema Crypto.com |
| **Gnosis (xDai)** | 100 | gnosisscan.io | Mercados de previsão |
| **zkSync Era** | 324 | explorer.zksync.io | L2 zero-knowledge |
| **Linea** | 59144 | lineascan.build | L2 da ConsenSys |

## Blockchains Account-Based Não-EVM

| Blockchain | Formato do endereço | Explorer | Particularidade |
|---|---|---|---|
| **Solana** | Base58 32-44 chars | solscan.io, explorer.solana.com | Alto volume de memecoins e scams; velocidade extrema |
| **Tron** | `T...` (Base58Check) | tronscan.org | Enorme volume de USDT — maior que Ethereum em transferências de stablecoin |
| **Ripple (XRP)** | `r...` | xrpscan.com, bithomp.com | Tags de destino identificam contas em exchanges |
| **Cosmos** | `cosmos1...` | mintscan.io | IBC interconecta chains |
| **Polkadot** | `1...` (SS58) | subscan.io | Parachains com explorers próprios |
| **TON** | `EQ...`, `UQ...` | tonscan.org | Popular na Rússia e Ásia; integração Telegram |
| **Algorand** | 58 chars alfanum | algoexplorer.io | — |
| **Near** | `nome.near` ou hash | explorer.near.org | Nomes legíveis podem facilitar identificação |
| **Cardano** | `addr1...` | cardanoscan.io | Modelo UTXO estendido (eUTXO) — híbrido |

## Fluxo de Análise Account-Based

```
1. IDENTIFICAR O ENDEREÇO E A BLOCKCHAIN
   └─ Confirmar rede (skill /blockchain-id se for 0x)
   └─ Verificar em DeBank se há atividade multi-chain

2. ANÁLISE DO ENDEREÇO (no explorer)
   ├─ Aba "Transactions" — moeda nativa (ETH, BNB, etc.)
   ├─ Aba "Token Transfers (ERC-20)" — CRÍTICA: movimentações de tokens
   │   (USDT, USDC, etc.) podem NÃO aparecer em "Transactions"
   ├─ Aba "Internal Transactions" — CRÍTICA: chamadas entre contratos
   │   que movem fundos internamente
   ├─ Aba "NFT Transfers" — movimentações de NFTs
   ├─ Aba "Analytics" (se disponível) — gráficos de balanço
   └─ Aba "Comments/Labels" — rótulos públicos (exchange, protocolo, etc.)

3. MAPEAR FLUXO DE TOKENS
   └─ Identificar QUAIS tokens foram movidos
   └─ Para cada token relevante:
      ├─ De onde veio (endereço origem ou contrato DEX)
      ├─ Para onde foi (destino, exchange, contrato DeFi)
      └─ Se passou por DEX: decodificar swap (token A → token B)

4. ANALISAR INTERAÇÕES COM CONTRATOS
   └─ DEX (Uniswap, PancakeSwap, Jupiter):
      ├─ Quais swaps (token A → token B)
      ├─ Valores
      └─ Pode indicar conversão de ativo rastreado
   └─ Bridge:
      ├─ Para qual blockchain os fundos foram
      ├─ Qual endereço recebeu na chain destino
      └─ Continuar rastreamento na chain destino (skill /cross-chain-tracing)
   └─ Mixer (Tornado Cash, Railgun):
      ├─ Registrar valor + timestamp do depósito
      ├─ Análise de timing/valor no saque
      └─ Sinalizar limitação

5. IDENTIFICAR PONTOS TERMINAIS
   └─ Exchanges centralizadas (endereços conhecidos — Arkham, labels)
   └─ Hot wallets (alto volume, muitas counterparts)
   └─ Carteiras pessoais (baixa atividade)
   └─ Contratos DeFi (fundos "estacionados")

6. VERIFICAR MULTI-CHAIN
   └─ Mesmo endereço 0x pode ter atividade em várias redes EVM
   └─ Verificar cada rede relevante
```

## Categorias de Ativos

### Moedas Nativas
ETH, BNB, SOL, TRX, MATIC — aparecem nas transações regulares.

### Tokens Fungíveis (ERC-20, BEP-20, SPL, TRC-20)
Criados por cima da blockchain via contrato. Exemplos: USDT, USDC, DAI, SHIB, UNI.

**⚠️ Alerta:** O mesmo token existe em MÚLTIPLAS blockchains. USDT Ethereum (ERC-20) ≠ USDT Tron (TRC-20) ≠ USDT BSC (BEP-20). São ativos tecnicamente distintos. Bridges permitem mover entre redes — frequente ponto de ofuscação.

### Stablecoins — Atenção Investigativa Especial

| Stablecoin | Lastro | Emissor | Congelamento |
|---|---|---|---|
| **USDT (Tether)** | Dólar | Tether Ltd. | ✅ Pode congelar endereços (blacklist on-chain) |
| **USDC** | Dólar (auditado) | Circle | ✅ Pode congelar endereços |
| **DAI** | Cripto colateralizado | MakerDAO | ❌ Descentralizado — NINGUÉM pode congelar |
| **BUSD** | Dólar | Paxos/Binance | Em phase-out |
| **FRAX, LUSD, crvUSD** | Variados | Variados | Geralmente descentralizados |

**Ponto investigativo:** emissores de USDT e USDC já congelaram endereços a pedido de autoridades. Verificar blacklist chamando `isBlacklisted()` no contrato do token.

### NFTs (ERC-721, ERC-1155)
- Wash trading entre carteiras do mesmo controlador = lavagem
- NFTs de alto valor podem ser veículo de transferência patrimonial
- Ferramentas: OpenSea, Blur, Magic Eden, NFTScan

## Orientação ao Investigador — Coleta no Etherscan (e similares)

Peça ao investigador:

> "Acesse [explorer da blockchain correta] e cole o endereço. Me envie:
> 1. **Overview**: saldo ETH/BNB/etc., saldo em tokens (aba Token Holdings)
> 2. **Transactions**: últimas 30 transações ou do período investigado
> 3. **Token Transfers (ERC-20)**: CRÍTICO — qualquer movimentação de USDT/USDC/outros
> 4. **Internal Txns**: se o endereço interagiu com contratos (DeFi, bridges)
> 5. **NFT Transfers**: se houver
> 6. Se o endereço tiver um **label** (tag pública), me avise
> 7. Se possível, exporte o CSV das transações
>
> Se o endereço interagiu com uma DEX (Uniswap, PancakeSwap), clique na transação e me envie a seção **'Tokens Transferred'** completa — ela mostra qual token entrou e qual saiu no swap."

## Interpretação de Transações Complexas

Uma transação EVM pode conter:
- **Main TX**: a chamada inicial (ex.: usuário chama `swapExactTokensForTokens()` na Uniswap)
- **Internal txns**: chamadas que o contrato faz a outros contratos (ex.: Uniswap chama o contrato do token para mover USDT)
- **Token transfers**: eventos `Transfer` emitidos (ex.: USDT foi de A para pool, ETH foi de pool para A)
- **Logs/Events**: outros eventos emitidos (ex.: `Swap(pool, amountIn, amountOut)`)

Para decodificar uma transação complexa no Etherscan, vá em "State Changes" e "Logs" — mostram exatamente o que cada conta ganhou ou perdeu.

## Ferramentas Avançadas

| Ferramenta | Especialidade | Acesso |
|---|---|---|
| **Arkham Intelligence** | Deanonymização, entidades, multi-chain | platform.arkham.intelligence |
| **Nansen** | Smart money, labels, analytics | nansen.ai (pago) |
| **DeBank** | Portfolio multi-chain EVM | debank.com |
| **Zapper** | Dashboard DeFi | zapper.xyz |
| **Dune Analytics** | Queries SQL on-chain | dune.com |
| **Breadcrumbs** | Visualização de fluxo | breadcrumbs.app |
| **Metasleuth** | Rastreamento visual multi-chain | metasleuth.io |
| **Revoke.cash** | Verificar e revogar aprovações de token | revoke.cash |

## Integração com outros skills

- Endereço 0x sem blockchain definida: `/blockchain-id` primeiro
- Fundos atravessam blockchains: `/cross-chain-tracing`
- Analisar contrato de token suspeito: `/smart-contract-audit`
- Padrões comportamentais: `/on-chain-patterns`
- Gerar relatório final: `/investigation-report`
