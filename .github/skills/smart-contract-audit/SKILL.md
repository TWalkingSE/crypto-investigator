---
name: smart-contract-audit
description: >
  Análise de contratos inteligentes para identificar riscos, funções perigosas, 
  backdoors e comportamento suspeito. Use quando o usuário pedir avaliação de 
  um contrato de token, suspeita de rug pull, análise de honeypot, verificação 
  de red flags em código verificado, investigação de contratos proxy 
  (upgradeable), análise de funções como mint/pause/blacklist/transferOwnership. 
  Também cobre verificação de aprovações (approve) maliciosas e mecanismos de 
  taxa (fee/tax) ocultos ou abusivos.
---

# Análise de Smart Contracts — Red Flags Investigativas

## Quando Usar Este Skill

- Token suspeito de rug pull
- Análise preventiva antes de rastreamento
- Verificação de honeypot (não permite venda)
- Contrato com comportamento anômalo
- Investigação de roubo via `approve()` malicioso
- Análise de contrato proxy (upgradeable)

## Protocolo Inicial

1. Solicite: **endereço do contrato + blockchain**
2. Oriente o investigador a acessar o explorer correto (bscscan, etherscan, polygonscan, etc.)
3. Verifique se o código está **verificado** na aba "Contract"
4. Se não estiver verificado — isso já é um red flag ALTO
5. Analise funções críticas (tabela abaixo)
6. Use ferramentas automatizadas para triagem rápida

## Red Flags — Catálogo Completo

| Red Flag | O que significa | Risco | Como verificar no explorer |
|---|---|---|---|
| **`mint()` sem limite pelo owner** | Dono pode criar tokens infinitamente (diluição/scam) | CRÍTICO | Aba Contract → Read: buscar `mint`, `_mint`. Ver se é `onlyOwner` sem cap |
| **`pause()` / `blacklist()` pelo owner** | Dono pode congelar transferências | ALTO | Contract → Read: funções `paused`, `blacklisted` |
| **`setFee()` / `setTax()` ilimitado** | Taxas de 99% no swap (honeypot) | CRÍTICO | Write: buscar funções que alteram taxa; verificar valor máximo |
| **`transferOwnership()` recente** | Troca de dono — possível ocultação de criador | MÉDIO | Events: buscar `OwnershipTransferred` |
| **Código NÃO verificado** | Impossível auditar | ALTO | Aba Contract mostra apenas bytecode |
| **`selfdestruct()`** | Contrato pode ser destruído | ALTO | Read: buscar por `selfdestruct` ou `suicide` |
| **Proxy contract (upgradeable)** | Lógica pode ser alterada após deploy | MÉDIO | Verificar padrão `delegatecall` ou detect no Etherscan label "Proxy" |
| **`approve()` para endereço externo fixo** | Permite que terceiro drene tokens | CRÍTICO | Events: buscar `Approval` para endereço estranho |
| **Função `anti-bot` ou "max wallet"** | Pode bloquear venda de usuários específicos | MÉDIO | Read: `maxWallet`, `maxTransactionAmount`, `excludeFromFee` |
| **`renounceOwnership()` recente em token com backdoor** | Finge descentralização mas contrato já permite abuso | ALTO | Events: verificar OwnershipRenounced + analisar código |
| **Hidden mint via rebase/rewards** | Supply aumenta via mecanismo oculto | ALTO | Ler código de rebase/rewards |
| **Taxas diferentes para buy vs sell** | Honeypot — compra livre, venda travada | CRÍTICO | `_transfer()` com lógica condicional |
| **Blacklist de endereços** | Dono pode impedir venda de vítimas | ALTO | Mapping `_isBlacklisted` |
| **Contract sem `Ownable` aparente mas com funções `onlyOwner`** | Dono oculto via proxy ou custom | ALTO | Análise cuidadosa do código |

## Protocolo Detalhado de Análise

```
1. VERIFICAR DADOS BÁSICOS (explorer)
   ├─ Endereço do contrato
   ├─ Blockchain
   ├─ Código verificado? (SIM/NÃO — se não: RED FLAG ALTO)
   ├─ Data de deploy (muito recente + volume alto = suspeito)
   ├─ Creator (endereço que criou o contrato)
   ├─ Quantidade de holders (poucos holders com concentração alta = suspeito)
   └─ Supply total

2. ANALISAR CÓDIGO (aba Contract → Source)
   ├─ Identificar linguagem (Solidity, Vyper, etc.)
   ├─ Listar imports (OpenZeppelin é sinal positivo)
   ├─ Buscar funções críticas (tabela de red flags)
   ├─ Verificar modifier `onlyOwner` e quem é o owner
   └─ Analisar eventos emitidos

3. VERIFICAR INTERAÇÕES RECENTES
   ├─ Últimas transações do contrato
   ├─ Mudanças de owner recentes
   ├─ Funções administrativas chamadas recentemente
   └─ Remoção de liquidez (especialmente red flag em tokens)

4. CROSS-CHECK COM FERRAMENTAS AUTOMATIZADAS
   ├─ Token Sniffer
   ├─ De.Fi Scanner
   ├─ GoPlus
   ├─ Honeypot.is (para honeypots)
   └─ StaySAFU

5. ANALISAR LIQUIDEZ (se for token)
   ├─ Em qual DEX tem pool? (Uniswap, PancakeSwap, etc.)
   ├─ Liquidez está lockada? (team-finance, unicrypt, pinksale)
   ├─ Quem detém os LP tokens? (se dev detém: ALTO RISCO)
   └─ Histórico: alguém removeu liquidez grande recentemente?

6. CLASSIFICAR RISCO E DOCUMENTAR
   ├─ CRÍTICO / ALTO / MÉDIO / BAIXO
   ├─ Listar red flags encontrados com evidência
   └─ Recomendar ações
```

## Ferramentas Automatizadas

| Ferramenta | O que faz | URL | Grátis? |
|---|---|---|---|
| **Token Sniffer** | Detecção automatizada de scams | tokensniffer.com | ✅ |
| **De.Fi Scanner** | Auditoria automatizada de contratos | de.fi/scanner | ✅ |
| **GoPlusLabs** | API de segurança para tokens | gopluslabs.io | ✅ |
| **Honeypot.is** | Verifica se token é honeypot | honeypot.is | ✅ |
| **StaySAFU** | Scanner de rug pull | staysafu.org | ✅ |
| **RugDoc** | Auditoria de farms e pools | rugdoc.io | ✅ |
| **CertiK Skynet** | Monitoramento contínuo | skynet.certik.com | ✅ limitado |
| **Slither** (CLI) | Análise estática em Solidity | github.com/crytic/slither | ✅ open-source |
| **Mythril** (CLI) | Análise simbólica | github.com/ConsenSys/mythril | ✅ open-source |

## Verificação de Aprovações Maliciosas (Revoke)

Se um investigado ou vítima teve tokens drenados via aprovação maliciosa:

1. Acesse **revoke.cash** com o endereço da vítima
2. Lista todas as aprovações ativas (tokens que terceiros podem gastar)
3. Identifica aprovações suspeitas (contratos desconhecidos com allowance infinita)
4. Permite revogar — a vítima pode limpar aprovações

Contratos maliciosos comuns:
- Ledger Connect falso
- Permit2 phishing
- MetaMask clone
- Site fake de airdrop

## Contratos Proxy (Upgradeable)

Contratos proxy delegam chamadas para um "contrato de implementação" que pode ser trocado pelo admin. Isso permite upgrade — mas também **permite que a lógica seja trocada por código malicioso após o deploy inicial**.

Como identificar:
- Label "Proxy" no Etherscan
- Função `implementation()` pública
- Eventos `Upgraded(address indexed implementation)`
- Padrão OpenZeppelin: `_IMPLEMENTATION_SLOT`

Ferramenta: **usb.guide** detecta e analisa proxies.

## Modelo de Relatório de Análise

```
🔍 ANÁLISE DE CONTRATO

Endereço: [0x...]
Blockchain: [rede]
Data de deploy: [data]
Creator: [endereço]
Código verificado: [SIM/NÃO]
Supply total: [valor]
Holders: [número]

🚩 RED FLAGS IDENTIFICADOS:
• [CRÍTICO] [descrição + trecho de código]
• [ALTO] [descrição + evidência]
• [MÉDIO] [descrição]

📊 ANÁLISE DE LIQUIDEZ:
• DEX: [Uniswap/PancakeSwap/etc.]
• Pool: [endereço]
• Liquidez atual: [$]
• LP tokens lockados: [SIM/NÃO + por quem]

⚙️ FERRAMENTAS AUTOMATIZADAS (resultados):
• Token Sniffer: [score ou veredicto]
• De.Fi Scanner: [resultado]
• Honeypot.is: [resultado]

🎯 VEREDICTO:
[RUGPULL CONFIRMADO / HONEYPOT / ALTO RISCO / RISCO MÉDIO / BAIXO RISCO]

Justificativa: [síntese]

📋 AÇÕES RECOMENDADAS:
1. [ação]
2. [ação]
```

## Integração com outros skills

- Padrões de golpe associados (rug pull, honeypot): `/scam-patterns`
- Rastrear fundos do contrato fraudulento: `/account-tracing` + `/cross-chain-tracing`
- Padrões on-chain pós-exploit: `/on-chain-patterns`
- Gerar relatório estruturado: `/investigation-report`
