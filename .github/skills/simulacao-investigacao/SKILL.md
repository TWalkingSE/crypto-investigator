---
name: simulacao-investigacao
description: >
  Cenários de investigação simulados para prática guiada. Use quando o 
  investigador quiser treinar análise on-chain com dados fictícios. Cria 
  casos com endereços, valores, timestamps e contexto investigativo. 
  Cobre: rastreamento Bitcoin simples, DeFi em Ethereum, investigação 
  cross-chain, rug pull, lavagem via mixer, fraude com stablecoins 
  multi-chain, wash trading de NFT. Após o investigador tentar resolver, 
  apresenta gabarito completo com mapa de fluxo e análise.
---

# Simulações de Investigação — Prática Guiada

## Quando Usar

Investigador quer praticar metodologia sem casos reais. Útil para:
- Treinamento interno de equipe
- Capacitação de novos investigadores
- Aperfeiçoamento técnico em áreas específicas
- Testar hipóteses em ambiente seguro

## Protocolo

1. Pergunte o nível: **Básico / Intermediário / Avançado**
2. Pergunte o tipo: **UTXO / Account / Cross-chain / DeFi / Golpe específico**
3. Apresente o cenário com dados fictícios, contexto e questões
4. Aguarde tentativa do investigador
5. Apresente o gabarito com:
   - Mapa de fluxo completo
   - Padrões identificados (skill `/on-chain-patterns`)
   - Classificação de risco
   - Ações recomendadas

## Cenários Disponíveis

### CENÁRIO 1 — Rastreamento Bitcoin Básico (UTXO)
**Nível:** Básico
**Objetivo:** Praticar identificação de troco e heurística de co-spending

```
📁 CASO: Saque suspeito de exchange

Contexto: Um investigado sacou 2.0 BTC da Binance para o endereço
bc1q-ALVO em 05/03/2025 14:30 UTC. Rastrear o destino dos fundos.

Dados observados em blockchair.com/bitcoin:

Endereço: bc1q-ALVO
Saldo atual: 0.02 BTC

Transação única de saída (TX-1):
- Data: 05/03/2025 15:45 UTC
- Inputs:
  - bc1q-ALVO: 2.00 BTC
- Outputs:
  - bc1q-DEST1: 1.50 BTC
  - bc1q-CHANGE: 0.48 BTC
  - Taxa de rede: 0.02 BTC

Investigação adicional no endereço bc1q-DEST1:
- Recebeu: 1.50 BTC
- Enviou: 1.50 BTC (TX-2, 05/03 16:20 UTC)
  - Output único: bc1q-COINBASE (endereço conhecido do WalletExplorer
    como hot wallet da Coinbase)

Investigação adicional no endereço bc1q-CHANGE:
- Recebeu: 0.48 BTC
- Saldo atual: 0.02 BTC (endereço da carteira alvo — mesmo cluster)

Tarefa:
1. Identifique qual output foi pagamento e qual foi troco. Justifique.
2. Monte o mapa de fluxo completo.
3. Quais diligências recomendaria?
```

**GABARITO 1:**
```
ANÁLISE:

1. Identificação de troco:
- bc1q-DEST1 recebeu 1.50 BTC e movimentou em seguida para Coinbase
  → esse é o PAGAMENTO (destino real)
- bc1q-CHANGE recebeu 0.48 BTC e está associado ao mesmo cluster
  do bc1q-ALVO → esse é o TROCO
- Heurística confirmatória: 1.50 é valor "redondo"; 0.48 é "quebrado"

2. Mapa de fluxo:

[Binance (CEX)]
    │ 2.00 BTC (05/03 14:30)
    ▼
[bc1q-ALVO]
    │
    ├─ 1.50 BTC (TX-1, 05/03 15:45) ──► [bc1q-DEST1]
    │                                        │
    │                                        └─ 1.50 BTC (TX-2, 16:20)
    │                                             ──► [Coinbase hot wallet]
    │                                                  ⚡ PONTO DE IDENTIFICAÇÃO
    │
    └─ 0.48 BTC (troco) ──► [bc1q-CHANGE] (mesmo cluster do ALVO)

3. Diligências:
- Requisição judicial à Coinbase com endereço de depósito bc1q-COINBASE
  e janela temporal 05/03 16:00-17:00 UTC
- Solicitar: titular da conta, KYC, IPs de acesso, método de saque
  posterior (se houve conversão para fiat)
- Verificar se bc1q-DEST1 pertence a outro cluster (pode ser
  conta intermediária de outro usuário)

Padrões (/on-chain-patterns):
- Round-numbered payment vs. change
- Consolidação pré-exchange (2 hops até exchange)
```

---

### CENÁRIO 2 — DeFi em Ethereum
**Nível:** Intermediário
**Objetivo:** Praticar leitura de swaps em DEX e token transfers

```
📁 CASO: Conversão suspeita de USDT em ETH

Contexto: Empresa X detectou saída não autorizada de 100.000 USDT
da carteira corporativa 0xCORP-1111 em 09/02/2025. Rastrear.

Dados observados em etherscan.io:

Endereço: 0xCORP-1111
Saldo USDT atual: 0
Última transação relevante:

TX principal: 0xaaa...111
- Data: 09/02/2025 03:17 UTC
- From: 0xCORP-1111
- To: 0xINT-2222 (endereço externo, não é contrato)
- Value: 0 ETH
- Token Transfers:
  - 100.000 USDT de 0xCORP-1111 para 0xINT-2222

Endereço: 0xINT-2222 — análise
- Saldo atual: 0 USDT, 0.15 ETH
- Token Transfers recentes mostram:

TX 0xbbb...222:
- Data: 09/02/2025 03:19 UTC
- From: 0xINT-2222
- To: 0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984 (contrato Uniswap V3)
- Value: 0 ETH
- Token Transfers:
  - 100.000 USDT de 0xINT-2222 para pool Uniswap
  - 52.3 ETH de pool Uniswap para 0xINT-2222

TX 0xccc...333:
- Data: 09/02/2025 03:24 UTC
- From: 0xINT-2222
- To: 0xSTARGATE... (contrato Stargate Bridge)
- Value: 52.3 ETH
- Events: "Swap" para Arbitrum, srcAddress = 0xINT-2222,
  dstAddress = 0xINT-2222

Tarefa:
1. Reconstrua o fluxo completo
2. Identifique padrões (/on-chain-patterns)
3. Quais diligências priorizaria?
4. Onde o rastreamento precisa continuar?
```

**GABARITO 2:**
```
ANÁLISE:

1. Fluxo completo:

[0xCORP-1111] ── carteira corporativa
    │ 100.000 USDT (TX-aaa, 03:17 UTC)
    ▼
[0xINT-2222] ── carteira intermediária (pessoal?)
    │ Swap via Uniswap V3 (TX-bbb, 03:19 UTC)
    │ 100.000 USDT → 52.3 ETH
    ▼
[0xINT-2222] ── mesmo endereço, agora com ETH
    │ Bridge via Stargate (TX-ccc, 03:24 UTC)
    │ 52.3 ETH Ethereum → Arbitrum
    ▼
[0xINT-2222 na ARBITRUM] ← RASTREAMENTO CONTINUA LÁ

2. Padrões:
- TOKEN SWAP IMEDIATO (2 minutos entre recebimento e swap USDT→ETH)
  → tentativa de converter ativo rastreável em outro
- BRIDGE HOP (5 minutos entre swap e bridge)
  → ofuscação cross-chain
- Timeline muito rápida (7 minutos do início ao fim)
  → operação provavelmente automatizada ou planejada

3. Diligências prioritárias:
a) Continuar rastreamento em Arbitrum — acessar arbiscan.io
   com o mesmo endereço 0xINT-2222 e verificar o que aconteceu
   após 03:24 UTC
b) Analisar 0xINT-2222: é carteira pessoal ou hot wallet de
   serviço? Verificar Arkham/Debank para labels
c) Correlacionar com logs de acesso da carteira corporativa
   (SIM swap? Phishing? Insider threat?)
d) Verificar se Tether pode blacklist o endereço 0xINT-2222
   considerando evidências

4. Continuação do rastreamento:
O endereço 0xINT-2222 em Arbitrum provavelmente fez nova movimentação
(talvez para exchange). O investigador deve:
- Acessar arbiscan.io, cole 0xINT-2222
- Verificar aba Transactions e Internal Txns a partir de 09/02 03:24 UTC
- Identificar próximo destino
```

---

### CENÁRIO 3 — Rug Pull em BSC
**Nível:** Intermediário
**Objetivo:** Identificar rug pull e rastrear criador

```
📁 CASO: Token MOONSHIB2025 despencou — rug pull?

Contexto: Investidores perderam dinheiro após o token MOONSHIB2025
(0xTOKEN...) colapsar em 20/03/2025. Investigar se foi rug pull.

Dados coletados em bscscan.com:

Contrato: 0xTOKEN-999
- Deploy: 18/03/2025 (2 dias antes do colapso)
- Creator: 0xDEV-AAA
- Código: NÃO VERIFICADO
- Holders: 1.247 (no pico)
- Supply: 1.000.000.000 tokens

Pool de liquidez (PancakeSwap): 0xPOOL-777
- Par: MOONSHIB2025 / BNB
- Liquidez inicial: 10.000 MOONSHIB2025 + 50 BNB (deposit em 18/03 por 0xDEV-AAA)

Eventos críticos em 20/03/2025:
- 14:15 UTC: 0xDEV-AAA chamou `removeLiquidity()` no PancakeSwap
  → Recebeu 1.847 BNB (liquidez acumulada + taxa)
- 14:15 UTC: Preço do token despencou 99.8%
- 14:22 UTC: 0xDEV-AAA transferiu 1.800 BNB para 0xINT-BBB
- 14:30 UTC: 0xINT-BBB depositou 1.800 BNB em Tornado Cash (pool de 100 BNB)

Tarefa:
1. É rug pull? Quais evidências?
2. Trace o fluxo de fundos do dev
3. Próximos passos de investigação
```

**GABARITO 3:**
```
ANÁLISE:

1. É RUG PULL — evidências:
- Código NÃO verificado (red flag crítico)
- LP tokens NÃO foram lockados (dev detinha todos)
- Remoção de liquidez pelo dev coincide com colapso do preço
- Tempo de vida do token: 2 dias (ciclo típico de rug)
- Dev imediatamente moveu fundos para ofuscação (Tornado Cash)
- Alto número de holders comprando + zero atividade de dev em
  suporte pós-deploy

2. Fluxo de fundos:

[Investidores: ~$X em BNB]
    │ compras de MOONSHIB2025
    ▼
[Pool PancakeSwap: 50 BNB iniciais + acumulação]
    │ removeLiquidity() em 20/03 14:15
    ▼
[0xDEV-AAA] ── criador/deployer
    │ 1.847 BNB extraídos
    │ Transfer em 14:22 (7min depois)
    ▼
[0xINT-BBB] ── carteira intermediária
    │ Depósito em Tornado Cash em 14:30 (8min depois)
    │ Pool de 100 BNB — 18 depósitos
    ▼
[Tornado Cash] ❌ Rastreamento on-chain interrompido

3. Próximos passos:
a) Analisar o contrato 0xTOKEN-999 com Token Sniffer, De.Fi Scanner
   (mesmo não verificado, bytecode pode ser decompilado)
b) Verificar se 0xDEV-AAA criou outros tokens antes (padrão serial
   de rug pullers) — buscar Transactions do endereço
c) Arkham/Bubblemaps para identificar cluster do dev
d) Focar nos SAQUES do Tornado Cash pool de 100 BNB em timing
   compatível (janelas horárias seguintes) — deanonimização parcial
   é possível
e) Bitcoin Abuse / Chainabuse para reportar e cruzar com outros casos
f) Cooperar com comunidade — fóruns de vítimas podem ter leads
   (handles Telegram/Discord do dev, fotos de avatar, histórico)
```

---

### CENÁRIOS ADICIONAIS DISPONÍVEIS (sob demanda)

| ID | Tipo | Nível | Foco |
|---|---|---|---|
| 4 | Pig butchering multi-chain | Avançado | Análise de plataforma falsa + cash-out |
| 5 | Wash trading NFT | Intermediário | Identificar sham transactions |
| 6 | Ransomware BTC | Avançado | Bitcoin + mixer + exchange de saída |
| 7 | Fake airdrop + phishing | Intermediário | Análise de approve malicioso |
| 8 | Insider trading em listagem | Avançado | Timing + consolidação pré-anúncio |
| 9 | Exploit de flash loan | Avançado | Decodificar TX complexa |
| 10 | Exit scam de exchange | Avançado | Identificar padrão de drenagem |

Para pedir um cenário específico:
> "Me apresente o cenário [N] para prática"

Para criar cenário customizado:
> "Crie um cenário de [tipo de crime] em [blockchain] no nível [básico/intermediário/avançado]"

## Regras dos Cenários

- Todos os dados são **fictícios**
- Endereços seguem formato real mas são inventados
- Cenários inspirados em casos documentados publicamente
- Marcar sempre como **SIMULAÇÃO** no cabeçalho de qualquer relatório gerado
- Não reproduzir dados de casos reais sob investigação
