---
name: utxo-tracing
description: >
  Rastreamento forense em blockchains UTXO (Unspent Transaction Output).
  Use para investigação de endereços e transações em Bitcoin (BTC), Litecoin 
  (LTC), Bitcoin Cash (BCH), Dogecoin (DOGE), Dash, Zcash transparente (t1).
  Também use quando o tema envolver: clusterização de endereços Bitcoin, 
  identificação de troco (change detection), heurística de co-spending, 
  WalletExplorer, OXT.me, análise de inputs/outputs, carteiras HD, 
  Bech32/SegWit/Taproot, CoinJoin. Diferencia UTXO do modelo account-based.
---

# Rastreamento UTXO — Bitcoin e Similares

## Conceito Central: UTXO

**Como funciona:** Cada transação consome "saídas não gastas" anteriores (UTXOs) e cria novas saídas. É como pagar com cédulas — você entrega R$50, recebe R$30 de troco. O "troco" é uma nova UTXO vinculada ao remetente.

**Implicação investigativa crítica:**
- Uma transação Bitcoin pode ter **múltiplas entradas** (de diferentes endereços) e **múltiplas saídas** (para diferentes destinos + troco)
- **Heurística de co-spending**: se dois endereços aparecem como ENTRADAS na mesma transação, **provavelmente pertencem à mesma carteira/pessoa** (porque é necessário ter a chave privada de ambos para assinar)
- **Problema do troco**: uma das saídas geralmente é troco retornando ao remetente — identificar qual é pagamento e qual é troco é tarefa investigativa central
- **Endereços descartáveis**: carteiras HD (Hierarchical Deterministic) geram um novo endereço para cada transação, dificultando rastreamento visual

## Blockchains UTXO

| Blockchain | Moeda | Formato do endereço | Explorer principal |
|---|---|---|---|
| **Bitcoin** | BTC | `1...` (Legacy), `3...` (P2SH/SegWit), `bc1q...` (Bech32), `bc1p...` (Taproot) | blockchair.com, mempool.space, oxt.me |
| **Litecoin** | LTC | `L...`, `M...`, `ltc1q...` | blockchair.com/litecoin |
| **Bitcoin Cash** | BCH | `bitcoincash:q...` ou legacy `1...` | blockchair.com/bitcoin-cash |
| **Dash** | DASH | `X...` | blockchair.com/dash |
| **Zcash** | ZEC | `t1...` (transparente) ou `zs1...` (shielded) | blockchair.com/zcash |
| **Dogecoin** | DOGE | `D...` | blockchair.com/dogecoin |

**⚠️ Zcash shielded (`zs1...`) e CoinJoin reduzem rastreabilidade drasticamente — sinalize ao investigador.**

## Fluxo de Análise UTXO

```
1. IDENTIFICAR O ENDEREÇO ALVO
   └─ Obter endereço Bitcoin do investigado (exchange, relatório, apreensão)

2. CLUSTERIZAR
   └─ Usar WalletExplorer ou OXT.me para encontrar TODOS os endereços
      da mesma carteira (heurística de co-spending)
   └─ Resultado: lista de endereços controlados pela mesma entidade

3. MAPEAR ENTRADAS E SAÍDAS
   └─ Para cada transação relevante:
      ├─ ENTRADAS: de onde vieram os fundos? (quais UTXOs foram gastos)
      ├─ SAÍDAS: para onde foram?
      └─ TROCO: qual saída retornou ao remetente?

4. IDENTIFICAR TROCO (Change Detection)
   └─ Heurísticas:
      ├─ Output que retorna para endereço do mesmo cluster = troco
      ├─ Output com valor "quebrado" (ex.: 0.03847 BTC) vs. "redondo"
      │   (ex.: 0.5 BTC) — redondo tende a ser pagamento
      └─ Output reutilizado rapidamente pode ser troco

5. SEGUIR O FLUXO
   └─ Seguir os outputs de pagamento (não-troco) para os próximos hops
   └─ Repetir hop a hop até chegar a ponto identificável
      (exchange, serviço conhecido, endereço clusterizado)

6. IDENTIFICAR PONTOS TERMINAIS
   └─ Exchanges (WalletExplorer identifica clusters conhecidos)
   └─ Mixers (padrões: muitas entradas similares, outputs uniformes)
   └─ Serviços (casas de apostas, marketplaces)
```

## Ferramentas Especializadas em UTXO

| Ferramenta | Função | URL |
|---|---|---|
| **OXT.me** | Visualização de grafos de transações Bitcoin, co-spending, change detection | oxt.me |
| **WalletExplorer** | Clusterização — agrupa endereços da mesma carteira | walletexplorer.com |
| **Blockchair** | Multi-chain, filtros avançados, exportação de dados | blockchair.com |
| **Mempool.space** | Transações não confirmadas em tempo real | mempool.space |
| **Bitcoin Abuse** | Banco de dados de endereços reportados | bitcoinabuse.com |
| **Chainabuse** | Denúncias multi-chain de fraude | chainabuse.com |

## Orientação ao Investigador — Coleta de Dados

Quando o investigador precisar analisar um endereço Bitcoin, peça:

> "Para que eu analise este endereço, acesse **blockchair.com/bitcoin** e me envie:
> 1. **Overview**: saldo atual, total recebido, total enviado, primeira e última transação
> 2. **Transactions**: lista das últimas 20 transações (ou do período investigado)
> 3. Para cada transação relevante, clique e me envie:
>    - **Inputs**: quais endereços enviaram (co-spending: múltiplos inputs sugerem mesma carteira)
>    - **Outputs**: quais endereços receberam e quanto cada um
>    - Timestamp e fee
> 4. **Complementar**: rode o endereço em walletexplorer.com e me diga se aparece um cluster identificado
> 5. Se possível, exporte o CSV completo para análise mais profunda"

## Análise de Padrões UTXO

Padrões específicos que aparecem em rastreamento UTXO (use em conjunto com `/on-chain-patterns`):

| Padrão | Descrição | Indicativo |
|---|---|---|
| **Peeling chain** | Saques sequenciais pequenos de carteira grande, cada um para endereço diferente | Distribuição ou ofuscação |
| **Batch consolidation** | Muitos inputs pequenos consolidados em poucos outputs grandes | Carteira de exchange (hot wallet) |
| **Round-number payments** | Outputs em valores "redondos" (1 BTC, 0.5 BTC) | Pagamento comercial vs. troco |
| **CoinJoin pattern** | Múltiplas entradas de valor similar + outputs uniformes | Mixer (Wasabi, JoinMarket) |
| **Address reuse** | Mesmo endereço usado em múltiplas transações | Serviço centralizado ou prática insegura |

## CoinJoin e Ofuscação

CoinJoin (Wasabi Wallet, JoinMarket) combina múltiplas transações em uma única, quebrando o vínculo direto entrada → saída. Indicadores:

- Múltiplos inputs de valor igual (ex.: 20 inputs de 0.1 BTC cada)
- Múltiplos outputs do mesmo valor
- Pequena variação para representar taxas

**Postura investigativa:** Ferramentas especializadas (Chainalysis, TRM Labs, CipherTrace) têm capacidade parcial de desconstruir CoinJoin, mas rastreamento sem essas ferramentas geralmente é inviável. Foco nos pontos de entrada (depósito antes do CoinJoin) e saída (primeira movimentação após).

## Integração com outros skills

- Padrões comportamentais: `/on-chain-patterns`
- Se fundos cruzam para outra blockchain (wrapped BTC, bridges): `/cross-chain-tracing`
- Para gerar o relatório final: `/investigation-report`
- Para prática guiada: `/simulacao-investigacao`
