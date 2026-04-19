---
name: on-chain-patterns
description: >
  Catálogo de padrões comportamentais on-chain usados em investigações 
  forenses. Use para identificar: peeling chain, fan-out, fan-in, round-trip, 
  dormência seguida de movimento, fragmentação uniforme, timing coordenado, 
  token swap imediato, bridge hop, consolidação pré-exchange, depósito em 
  mixer, layering, integração. Cada padrão tem descrição, indicativo 
  comportamental e orientação investigativa. Reference rápida para 
  reconhecer ofuscação, lavagem, automação, wash trading, ou comprometimento 
  de chave.
---

# Padrões Comportamentais On-Chain — Catálogo

## Uso deste Skill

Este é um **catálogo de referência**. Use em qualquer análise para identificar padrões e nomear o comportamento observado. Os padrões são neutros — um mesmo padrão pode indicar uso lícito ou ilícito. O contexto determina.

## Catálogo Completo

### Peeling Chain
**Descrição:** Saques sequenciais de valores pequenos a partir de uma carteira grande, cada saque para um endereço diferente.

```
[Carteira grande: 100 BTC]
    │
    ├─ 0.5 BTC ──► [Endereço 1]
    │   remanescente: 99.5 BTC
    ├─ 0.3 BTC ──► [Endereço 2]
    │   remanescente: 99.2 BTC
    ├─ 0.7 BTC ──► [Endereço 3]
    │   remanescente: 98.5 BTC
    └─ ... (continua)
```

**Indicativo de:**
- Distribuição de fundos para múltiplos destinatários
- Ofuscação (layering) — dificulta rastreamento
- Sacador operando hot wallet de serviço

**Investigar:** Cada endereço destinatário individualmente; verificar se há padrão nos valores; identificar se destinatários convergem posteriormente.

---

### Fan-Out / Fan-In
**Descrição:** Fundos de um endereço se dividem para múltiplos (fan-out) e depois reconvergem para um único (fan-in).

```
Fan-Out:
[A] ──┬──► [B1]
      ├──► [B2]
      └──► [B3]

Fan-In:
[B1] ──┐
[B2] ──┼──► [C]
[B3] ──┘
```

**Indicativo de:**
- Tentativa de quebrar trilha e reconsolidar
- Layering clássico de lavagem
- Separação temporária para esfriamento (wait-and-consolidate)

**Investigar:** Identificar a carteira central de reconsolidação; o endereço C frequentemente é a próxima parada real (exchange, carteira operacional).

---

### Round-Trip
**Descrição:** Fundos saem do endereço A, passam por B, C, D, e retornam a A (ou a um endereço do mesmo cluster).

**Indicativo de:**
- Wash trading — inflar volume artificialmente
- Teste de rastreabilidade pelo próprio criminoso
- Criação de "histórico" falso de atividade
- Em NFTs: simulação de demanda inexistente

**Investigar:** Identificar se os endereços intermediários têm relação (mesmo cluster, mesma origem de gás, timing similar).

---

### Dormência seguida de movimento
**Descrição:** Endereço parado por meses ou anos que, de repente, movimenta tudo.

**Indicativo de:**
- Comprometimento de chave (hack, acesso a seed)
- Retomada de atividade pelo titular após período de cautela
- Herança/transferência pós-falecimento
- "Awakening" de whale — relevante em análise de mercado

**Investigar:** Analisar comportamento anterior vs. novo; verificar se o novo padrão é consistente com o titular conhecido; cruzar com eventos externos (hacks anunciados, prisões, etc.).

---

### Fragmentação Uniforme
**Descrição:** Valor é dividido em partes iguais (ou quase iguais) distribuídas para múltiplos endereços.

```
[A: 10 ETH]
    │
    ├─ 1 ETH ──► [B1]
    ├─ 1 ETH ──► [B2]
    ├─ 1 ETH ──► [B3]
    └─ ... (10 destinatários)
```

**Indicativo de:**
- Distribuição coordenada (pagamento de comissões, fees, rewards)
- Layering de lavagem
- Bot de distribuição automatizada
- CoinJoin (mas em UTXO, geralmente)

**Investigar:** Todos os destinatários foram ativos ao mesmo tempo? Algum deles convergiu posteriormente? Origem do endereço A (exchange, contrato, pessoal?).

---

### Timing Coordenado
**Descrição:** Múltiplas transações de endereços diferentes no mesmo minuto (ou bloco).

**Indicativo de:**
- Automação / bot
- Mesma pessoa controlando múltiplas carteiras
- Exploit coordenado (múltiplos endereços atacando mesmo contrato)
- Evento externo disparando reação (notícia, listagem de token)

**Investigar:** Origens de gas (quem pagou as fees de cada carteira? mesma origem?), padrão de nonces, relação entre endereços via Arkham/Bubblemaps.

---

### Token Swap Imediato
**Descrição:** Endereço recebe token A e converte para token B em segundos (via DEX).

**Indicativo de:**
- Tentativa de converter ativo rastreável (USDT) em outro menos rastreado (DAI, ETH)
- Arbitrage bot
- Reação automática a evento (fundos suspeitos precisam ser "lavados" rápido)

**Investigar:** Tempo exato entre recebimento e swap (segundos = provável bot); verificar se existe script/contrato entre os dois eventos; seguir o token de saída.

---

### Bridge Hop
**Descrição:** Fundos cruzam para outra blockchain imediatamente após recebimento.

**Indicativo de:**
- Ofuscação cross-chain (dificultar rastreamento em explorer único)
- Uso de liquidez em outra rede (ex.: USDT Tron é mais líquido que BSC)
- Destino final é exchange/serviço específico da chain destino

**Investigar:** Qual bridge usado? Qual endereço recebeu na chain destino? Continuar rastreamento com `/cross-chain-tracing`.

---

### Consolidação Pré-Exchange
**Descrição:** Múltiplos endereços enviam para um endereço central, que em seguida deposita em exchange.

```
[End 1] ──┐
[End 2] ──┼──► [Endereço central] ──► [Hot wallet de exchange]
[End 3] ──┤
[End 4] ──┘
```

**Indicativo de:**
- Juntar fragmentos antes de cash-out
- Fim de fluxo de lavagem (integração)
- Operador recolhendo rendas de múltiplas fontes

**Investigar:** Identificar a exchange (Etherscan/explorer label + Arkham); requisitar dados da conta que recebeu o depósito — ponto de identificação humana.

---

### Depósito em Mixer
**Descrição:** Valor depositado em contrato de mixer (Tornado Cash, Railgun, Cyclone).

**Indicativo de:**
- Tentativa de quebrar vínculo on-chain
- Caso de lavagem grave (Tornado Cash é sancionado)
- Proteção legítima de privacidade (caso raro em investigações)

**Investigar:**
- Registrar valor exato, timestamp, denominação (Tornado Cash usa pools de 0.1/1/10/100 ETH)
- Tentar correlacionar com saques na mesma denominação em timing compatível
- Ferramentas institucionais (Chainalysis, TRM) têm capacidade parcial de deanonimizar
- Foco em pontos de entrada (antes do mixer) e saída (depois)

---

### Layering Clássico (3 Estágios de Lavagem)
**Descrição:** Ofuscação estruturada em camadas para distanciar origem criminosa de destino final.

```
PLACEMENT (colocação):
└─ Origem criminosa → cripto (via P2P, cartão pré-pago)

LAYERING (ocultação):
└─ Múltiplos swaps + bridges + mixers + peeling

INTEGRATION (integração):
└─ Cash-out em exchange (fiat) + compra de ativo legítimo
```

**Indicativo de:** Operação profissional de lavagem.

**Investigar:** Quebrar cada estágio separadamente; foco nos pontos de entrada e saída do layering; identificar padrões da operação (timing, valores, ferramentas preferidas).

---

### Address Reuse (Reutilização de Endereço)
**Descrição:** Mesmo endereço usado em múltiplas transações ao longo do tempo.

**Indicativo de:**
- Serviço centralizado (exchange, wallet web)
- Usuário com pouca sofisticação em privacidade
- Endereço "público" de entidade (fundação, DAO, projeto)
- Vantagem investigativa — permite análise consolidada

**Investigar:** Mapear histórico completo; verificar se é endereço conhecido (label público, Arkham).

---

### Batch Transaction (Transação em Lote)
**Descrição:** Uma única transação com muitos outputs/destinatários (UTXO) ou múltiplas chamadas internas (account-based).

**Indicativo de:**
- Exchange processando saques em lote (economiza fee)
- Contrato distribuindo tokens (airdrop, rewards)
- Operação eficiente, não necessariamente ilícita

**Investigar:** Identificar origem (exchange? contrato? pessoal?); lista de destinatários pode ser longa — triagem por valor e pelo comportamento subsequente.

---

### Sandwich Attack (em DeFi)
**Descrição:** Bot detecta transação pendente de swap na mempool e coloca transações "antes" e "depois" para extrair valor (MEV).

**Indicativo de:** MEV/arbitragem automatizada — não é golpe no sentido clássico, mas é extrativo.

**Investigar:** Ferramenta: mev-explore.pics, eigenphi.io para histórico de MEV por endereço.

---

### Flash Loan em bloco único
**Descrição:** Empréstimo de milhões sem colateral, usado e devolvido no mesmo bloco.

**Indicativo de:**
- Exploit de protocolo (frequente em hacks)
- Arbitragem avançada
- Manipulação de preço de oracle

**Investigar:** Decodificar a sequência de eventos no mesmo TX; ferramentas como Phalcon/Tenderly ajudam a visualizar.

---

## Como Usar na Análise

1. Observe o comportamento nos dados
2. Identifique o(s) padrão(ões) que melhor descrevem
3. Na seção 4 do relatório (`/investigation-report`), nomeie explicitamente
4. Vincule cada padrão à evidência concreta (transação específica, valores, datas)
5. Interprete considerando o contexto

## Exemplo de Aplicação

```
SEÇÃO 4 — ANÁLISE DE PADRÕES (INFERÊNCIAS)

Padrões observados:
• PEELING CHAIN — Entre 01/03 e 15/03/2025, o endereço 0xABC enviou
  12 saques de valores entre 0.1 e 0.3 ETH para endereços distintos.
  Compatível com distribuição ou ofuscação.

• BRIDGE HOP — Em 09/03/2025 03:24 UTC, imediatamente após receber
  52.3 ETH, o endereço executou bridge via Stargate para Arbitrum
  (TX 0xjkl...abc). Tempo entre recebimento e bridge: 5 minutos.
  Compatível com automação ou operação planejada.

• CONSOLIDAÇÃO PRÉ-EXCHANGE — Os endereços 0xINT1 e 0xINT2
  convergiram para 0xFINAL3, que depositou 52.3 ETH em hot wallet
  da Coinbase em 09/03/2025 04:00 UTC. Ponto de identificação
  humana via requisição judicial.

Hipótese investigativa (confiança: ALTA):
Os padrões combinados (bridge hop + consolidação + timing coordenado)
são consistentes com operação de lavagem estruturada para quebrar
rastreabilidade em explorer único e realizar cash-out em exchange.
```

## Integração com outros skills

- Padrões observados em UTXO: `/utxo-tracing`
- Padrões em account-based: `/account-tracing`
- Cross-chain patterns específicos: `/cross-chain-tracing`
- Classificar como esquema específico: `/scam-patterns`
- Documentar no relatório: `/investigation-report`
