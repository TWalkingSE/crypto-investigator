---
name: cross-chain-tracing
description: >
  Rastreamento complexo envolvendo múltiplos saltos (hops), conversões entre 
  tokens, bridges entre blockchains, DeFi e mixers. Use quando fundos cruzam 
  de uma rede para outra (Ethereum → BSC, Polygon → Arbitrum, etc.), passam 
  por DEX (Uniswap, PancakeSwap, Jupiter), atravessam bridges (Stargate, 
  Wormhole, Multichain, Hop, Across), interagem com lending (Aave, Compound), 
  ou são depositados em mixers (Tornado Cash, Railgun). Ensina a manter a 
  trilha investigativa quando o caminho dos fundos passa por múltiplas redes 
  e protocolos.
---

# Rastreamento Cross-Chain e Multi-Hop

## Quando Usar

- Fundos saem de uma blockchain e aparecem em outra (bridge)
- Conversões entre tokens via DEX
- Interação com protocolos DeFi (lending, yield, LP)
- Passagem por mixers ou protocolos de privacidade
- Investigação com 3+ saltos (hops) sequenciais

## Protocolo de Rastreamento Multi-Hop

```
1. MAPEAR O CAMINHO COMPLETO
   └─ Origem → hops intermediários → destino
   └─ Para cada hop identificar:
      ├─ Blockchain
      ├─ Tipo de operação (transfer, swap, bridge, lending, mixer)
      ├─ Valor e token
      ├─ Timestamp
      └─ Contraparte (endereço ou contrato)

2. AO CRUZAR BLOCKCHAIN (bridge)
   └─ Identificar protocolo de bridge usado
   └─ Rastrear depósito na chain de ORIGEM
   └─ Buscar endereço e valor na chain de DESTINO
   └─ Continuar rastreamento na chain destino

3. AO PASSAR POR DEX
   └─ Decodificar swap: qual token entrou, qual saiu
   └─ Verificar endereço do pool
   └─ Seguir o token de saída para o próximo hop

4. AO DEPOSITAR EM MIXER
   └─ Registrar valor, timestamp, denominação (Tornado Cash usa denominações fixas)
   └─ Sinalizar ruptura de rastreamento
   └─ Focar em pontos de entrada (antes do mixer) e saída (depois)

5. GERAR MAPA TEXTUAL COMPLETO
   └─ Use o formato de mapa de fluxo (ver abaixo)

6. IDENTIFICAR INCERTEZAS
   └─ Onde o rastreamento é sólido
   └─ Onde há perda de trilha (mixer, privacy coin)
   └─ Que diligências adicionais resolvem cada incerteza
```

## Protocolos de Bridge

| Bridge | Chains suportadas | Como rastrear |
|---|---|---|
| **Stargate** | Ethereum, BSC, Polygon, Avalanche, Arbitrum, Optimism, Base, + | Depósito emite evento; busca no explorer de destino pelo valor + timestamp |
| **Wormhole** | 30+ chains incluindo Solana, Ethereum, BSC | wormholescan.io para rastrear mensagens cross-chain |
| **Multichain/AnySwap** | Muitas EVM | ⚠️ Hackeado em 2023; muitos fundos ainda pendentes. Rastreamento limitado |
| **Hop Protocol** | L2s (Arbitrum, Optimism, Polygon) | explorer.hop.exchange |
| **Across** | Ethereum e L2s | across.to |
| **Synapse** | Multi-chain | explorer.synapseprotocol.com |
| **cBridge (Celer)** | Multi-chain | cbridge.celer.network |
| **Polygon Bridge** | Ethereum ↔ Polygon | Verificar depósito/saque nos contratos oficiais |
| **Arbitrum Bridge** | Ethereum ↔ Arbitrum | bridge.arbitrum.io |
| **Base Bridge** | Ethereum ↔ Base | bridge.base.org |
| **LayerZero** | Camada de mensageria entre chains | layerzeroscan.com |

**⚠️ Atenção:** muitos bridges oferecem transferências instantâneas via pools de liquidez. O endereço de destino pode não ser o mesmo de origem — o bridge pode entregar para qualquer endereço indicado pelo usuário.

## DEXs Principais por Chain

| DEX | Chain principal | Explorer de swaps |
|---|---|---|
| **Uniswap (V2/V3/V4)** | Ethereum, L2s, Polygon | etherscan.io, dextools.io |
| **PancakeSwap** | BSC | bscscan.com, dextools.io |
| **SushiSwap** | Multi-chain | sushi.com/analytics |
| **Curve** | Ethereum, + | curve.fi/#/ethereum |
| **Balancer** | Ethereum, Arbitrum, + | balancer.fi |
| **Jupiter** | Solana | jup.ag |
| **Raydium** | Solana | raydium.io |
| **Orca** | Solana | orca.so |
| **SunSwap** | Tron | sunswap.com |
| **1inch (agregador)** | Multi-chain | 1inch.io — rotas através de múltiplas DEXs |
| **Paraswap (agregador)** | Multi-chain | paraswap.io |
| **0x (agregador)** | Multi-chain | 0x.org |

## Protocolos DeFi Complexos

| Tipo | Exemplos | Como é usado para ofuscar | Como investigar |
|---|---|---|---|
| **Lending** | Aave, Compound, Venus (BSC) | Depositar colateral, sacar outro ativo | Rastrear depósitos/saques no contrato; verificar internal txns |
| **Flash loans** | Aave, dYdX, Uniswap | Operações complexas em bloco único | Decodificar sequência de eventos no mesmo TX |
| **Yield farming / LP** | Uniswap LP, Curve, Convex | Depositar em pools — fundos "estacionados" | Rastrear LP tokens recebidos; monitorar saída |
| **Vaults** | Yearn, Beefy | Depositar em vault que gerencia estratégia | Rastrear token de recibo (yToken, etc.) |
| **Aggregators** | 1inch, Paraswap | Roteiam por múltiplas DEXs | Decodificar TX para ver DEXs usadas |

## Mixers e Protocolos de Privacidade

| Protocolo | Tipo | Rastreabilidade | Nota investigativa |
|---|---|---|---|
| **Tornado Cash** | Smart contract (Ethereum, BSC, Polygon) | Depende de timing/valor | ⚠️ Sancionado OFAC. Chainalysis e TRM conseguem deanonymizar parcialmente em casos de uso grosseiro (saque rápido, valores distintos) |
| **Railgun** | Smart contract multi-chain | Muito baixa | Usa zk-proofs — análise complexa |
| **Cyclone** | Fork de Tornado | Depende de timing/valor | Similar ao Tornado |
| **Aztec Network** | zkRollup com privacidade | Muito baixa | zk-SNARKs — rastreamento inviável sem cooperação |
| **Monero (XMR)** | Blockchain nativa | Muito baixa | Ring signatures, stealth addresses, RingCT — foco em entry/exit points |
| **Zcash shielded** | Blockchain nativa | Muito baixa se for shielded | Maioria das TX Zcash são transparentes (t1) — verificar tipo |

**Postura investigativa com privacidade:**
Quando fundos passam por mixer ou privacy coin, o rastreamento on-chain pode ser inviável. Foque em:
1. **Ponto de entrada**: qual exchange/serviço recebeu depósito antes do mixer?
2. **Ponto de saída**: qual exchange/serviço recebeu após o saque?
3. **Timing e valor**: registros exatos de quando e quanto foi depositado vs. sacado
4. **Exchanges com KYC** são o elo mais frágil da cadeia de privacidade

## Mapa de Fluxo Textual — Modelo

Quando a análise envolver múltiplos hops, forneça mapa textual:

```
MAPA DE FLUXO DE FUNDOS

[Exchange Binance (CEX)]
    │ 100.000 USDT ─── TX: 0xabc...123 (09/02/2025 03:17 UTC) [Ethereum]
    ▼
[0xCORP...1111] ◄── Carteira corporativa comprometida
    │ 100.000 USDT ─── TX: 0xdef...456 (03:19 UTC) [Ethereum]
    ▼
[0xINT1...2222] ── Carteira intermediária
    │ Swap via Uniswap V3
    │ 100.000 USDT → 52.3 ETH ─── TX: 0xghi...789 (03:19 UTC)
    ▼
[0xINT1...2222] ── mesma carteira, agora com ETH
    │ Bridge via Stargate
    │ 52.3 ETH Ethereum → Arbitrum ─── TX: 0xjkl...abc (03:24 UTC)
    ▼
[0xINT1...2222 em Arbitrum] ── CRUZOU DE REDE
    │ 52.3 ETH ─── TX: 0xmno...def (03:31 UTC) [Arbitrum]
    ▼
[0xFINAL...3333 em Arbitrum]
    │ 52.3 ETH ─── TX: 0xpqr...ghi (04:00 UTC)
    ▼
[Hot wallet Coinbase (CEX)] ◄── PONTO DE IDENTIFICAÇÃO
    ⚡ Diligência: requisição judicial à Coinbase vinculando o endereço
       de depósito à identidade do titular da conta

RESUMO DA OFUSCAÇÃO:
• Conversão USDT → ETH (quebra de rastreabilidade por token)
• Bridge Ethereum → Arbitrum (quebra de rastreabilidade por rede)
• Carteira intermediária para dissociar origem e destino
• Tempo total: ~43 minutos — operação rápida, possivelmente automatizada

PONTO SÓLIDO: identificação da exchange de saída (Coinbase)
PONTO DE INCERTEZA: nenhum — cadeia completa e documentada
```

## Ferramentas para Investigação Cross-Chain

| Ferramenta | Especialidade | URL |
|---|---|---|
| **Arkham Intelligence** | Entidades multi-chain, labels | platform.arkham.intelligence |
| **Chainalysis Reactor** | Institucional (polícia, compliance) | Licença |
| **TRM Labs** | Forense, triagem de risco | Licença |
| **Elliptic** | Compliance, triagem | Licença |
| **Crystal Blockchain** | Análise de fluxo, pontuação | Licença |
| **Metasleuth (BlockSec)** | Visual multi-chain | metasleuth.io |
| **Misttrack (SlowMist)** | Fundos roubados, multi-chain | misttrack.io |
| **Breadcrumbs** | Visualização de fluxo | breadcrumbs.app |
| **DeBank** | Portfolio multi-chain EVM | debank.com |
| **DexScreener** | Monitoramento DEXs tempo real | dexscreener.com |
| **DEXTools** | Histórico swaps, top traders | dextools.io |
| **Bubblemaps** | Visualização de clusters e relações entre carteiras | bubblemaps.io |
| **Whale Alert** | Alertas de grandes movimentações | whale-alert.io |

## Integração com outros skills

- Origem UTXO (Bitcoin que vira WBTC): `/utxo-tracing` + este skill
- Análise do contrato do bridge ou DEX: `/smart-contract-audit`
- Esquema cross-chain suspeito (ponzi, rug pull): `/scam-patterns`
- Padrões observados: `/on-chain-patterns`
- Gerar relatório com múltiplos hops: `/investigation-report`
