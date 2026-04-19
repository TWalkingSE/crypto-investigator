---
name: roteiro-estudo
description: >
  Plano de aprendizado estruturado para investigadores que querem se capacitar 
  em investigação on-chain. Use quando o usuário pedir "por onde começar", 
  "roteiro de estudo", "como me capacitar em cripto", "quero aprender a 
  investigar criptoativos" ou quiser estruturar plano de carreira em 
  cibercrime cripto. Cria trilha por nível (iniciante, intermediário, 
  avançado) com módulos, exercícios, ferramentas e estimativas de tempo.
---

# Roteiro de Estudo — Investigação On-Chain

## Protocolo

1. Pergunte o nível atual: **Iniciante / Intermediário / Avançado**
2. Pergunte o contexto: **law enforcement, compliance, perícia, pesquisa acadêmica, aprendizado pessoal**
3. Apresente trilha adequada com módulos, tempo estimado e ferramentas
4. Sugira sequência de 3-6 meses para dominar o essencial

## Formato de Cada Módulo

```
📚 Módulo N: [Título]
Objetivo: [competência a desenvolver]
Conteúdo: [tópicos]
Prática: [exercício ou simulação]
Ferramentas: [o que usar]
Tempo estimado: [horas]
Recursos: [livros, cursos, artigos]
```

---

## TRILHA INICIANTE (sem conhecimento prévio em cripto)

### Módulo 1 — Fundamentos de Blockchain
- **Objetivo:** entender o que é blockchain, hash, chave pública/privada, endereços, transações
- **Conteúdo:** história do Bitcoin, white paper, proof-of-work, proof-of-stake, modelo UTXO vs. account
- **Prática:** criar carteira Bitcoin e Ethereum em testnet (Sepolia); executar transação
- **Ferramentas:** Electrum (BTC), MetaMask (ETH), Sepolia faucet
- **Tempo:** 10h
- **Recursos:**
  - Livro: "Mastering Bitcoin" (Andreas Antonopoulos) — cap. 1-4
  - Livro: "Mastering Ethereum" (Antonopoulos + Wood) — cap. 1-2
  - Vídeos: canal YouTube "3Blue1Brown" sobre Bitcoin (básico conceitual)

### Módulo 2 — Introdução aos Explorers
- **Objetivo:** saber ler qualquer explorer com confiança
- **Conteúdo:** interface do Etherscan, Blockchair, Mempool.space; abas principais; busca por hash/endereço
- **Prática:** analisar 5 endereços reais conhecidos (Vitalik Buterin, fundador Binance, exchange Coinbase)
- **Ferramentas:** Etherscan, BscScan, Blockchair, Mempool.space
- **Tempo:** 8h

### Módulo 3 — Modelo UTXO (Bitcoin)
- **Objetivo:** entender e rastrear em UTXO
- **Conteúdo:** inputs/outputs, change detection, co-spending heuristic, clusterização
- **Prática:** rastrear 2 transações Bitcoin reais via blockchair.com/bitcoin
- **Ferramentas:** Blockchair, OXT.me, WalletExplorer
- **Tempo:** 10h
- **Skill relacionado:** `/utxo-tracing`

### Módulo 4 — Modelo Account (Ethereum/EVM)
- **Objetivo:** rastreamento em EVM com tokens
- **Conteúdo:** nonce, gas, internal transactions, token transfers, allowances
- **Prática:** rastrear endereço com atividade DeFi no Etherscan
- **Ferramentas:** Etherscan, DeBank
- **Tempo:** 12h
- **Skill relacionado:** `/account-tracing`

### Módulo 5 — Problema do 0x e Multi-Chain
- **Objetivo:** não errar a rede na investigação
- **Conteúdo:** protocolo de identificação; DeBank; verificação cruzada
- **Prática:** analisar 3 endereços 0x em múltiplas redes EVM e documentar diferenças
- **Ferramentas:** DeBank, Arkham, Blockchair
- **Tempo:** 6h
- **Skill relacionado:** `/blockchain-id`

**Total trilha iniciante: ~46h (4-6 semanas em ritmo de 10h/semana)**

---

## TRILHA INTERMEDIÁRIA

### Módulo 6 — Tokens e DeFi Básico
- **Objetivo:** entender ERC-20, BEP-20, SPL; stablecoins; DEX
- **Conteúdo:** tokens vs. moeda nativa; swaps em Uniswap/PancakeSwap; lending básico
- **Prática:** decodificar TX de swap via Etherscan "State Changes"; identificar token in / token out
- **Ferramentas:** Etherscan, DexScreener, DEXTools
- **Tempo:** 15h

### Módulo 7 — Padrões Comportamentais
- **Objetivo:** reconhecer padrões on-chain
- **Conteúdo:** peeling chain, fan-out/in, round-trip, consolidação, bridge hop
- **Prática:** simular 3 cenários do skill `/simulacao-investigacao`
- **Ferramentas:** Breadcrumbs, Arkham
- **Tempo:** 10h
- **Skill relacionado:** `/on-chain-patterns`

### Módulo 8 — Bridges e Cross-Chain
- **Objetivo:** manter trilha quando fundos cruzam redes
- **Conteúdo:** como bridges funcionam; Stargate, Wormhole, Multichain, Hop; rastreamento cross-chain
- **Prática:** analisar um bridge real e encontrar o endereço de destino em outra rede
- **Ferramentas:** LayerZero Scan, Wormhole Scan, Stargate
- **Tempo:** 12h
- **Skill relacionado:** `/cross-chain-tracing`

### Módulo 9 — Mixers e Privacidade
- **Objetivo:** entender limites de rastreamento em Tornado Cash, Railgun, CoinJoin, Monero
- **Conteúdo:** mecanismos de privacidade; análise de timing; deanonimização parcial
- **Prática:** analisar histórico de Tornado Cash (período 2022-2024)
- **Ferramentas:** Etherscan, Chainalysis reports públicos
- **Tempo:** 10h

### Módulo 10 — Análise de Smart Contracts
- **Objetivo:** identificar red flags em tokens e contratos
- **Conteúdo:** mint/burn/pause, blacklist, ownership, proxy, honeypot
- **Prática:** auditar 3 tokens recém-deployados em BSC usando Token Sniffer + análise manual
- **Ferramentas:** Token Sniffer, De.Fi, Honeypot.is, Slither
- **Tempo:** 15h
- **Skill relacionado:** `/smart-contract-audit`

### Módulo 11 — Catálogo de Golpes
- **Objetivo:** reconhecer tipologias de crime cripto
- **Conteúdo:** rug pull, ponzi, phishing, pig butchering, ransomware, fake airdrop
- **Prática:** estudo de caso de 2 incidentes públicos (ex.: FTX collapse, Ronin Bridge hack)
- **Ferramentas:** Rekt.news, Chainalysis reports
- **Tempo:** 12h
- **Skill relacionado:** `/scam-patterns`

**Total trilha intermediária: ~74h (8-10 semanas)**

---

## TRILHA AVANÇADA

### Módulo 12 — Ferramentas Institucionais
- **Objetivo:** usar Chainalysis Reactor, TRM Labs, Elliptic (via trial ou convênio)
- **Conteúdo:** attribution, clustering proprietário, risk scoring, case management
- **Prática:** investigação completa em ambiente institucional com ferramenta profissional
- **Ferramentas:** Chainalysis, TRM, Elliptic (licença)
- **Tempo:** 25h

### Módulo 13 — Investigação Forense End-to-End
- **Objetivo:** conduzir caso do início (endereço suspeito) ao fim (relatório processual)
- **Conteúdo:** coleta, análise, cadeia de custódia, laudo, aceitação processual
- **Prática:** relatório completo sobre caso real documentado publicamente
- **Ferramentas:** todas anteriores + Maltego
- **Tempo:** 20h
- **Skill relacionado:** `/investigation-report`

### Módulo 14 — Persecução Patrimonial (Brasil)
- **Objetivo:** dominar o fluxo de localização → constrição → custódia → destinação
- **Conteúdo:** Lei 14.478/2022, IN 1.888/2019, alienação antecipada, cooperação internacional
- **Prática:** minuta de requisição judicial completa
- **Ferramentas:** legislação, Sisbajud (demonstração)
- **Tempo:** 15h
- **Skill relacionado:** `/persecucao-patrimonial`

### Módulo 15 — Programação para Investigação
- **Objetivo:** automatizar análises
- **Conteúdo:** Python + pandas para CSV; web3.py / ethers.js para queries on-chain; SQL em Dune
- **Prática:** script para detectar peeling chain em lista de endereços
- **Ferramentas:** Python, Foundry (cast), Dune Analytics
- **Tempo:** 30h

### Módulo 16 — Análise de Contratos Avançada
- **Objetivo:** auditar código complexo e identificar exploits
- **Conteúdo:** flash loans, reentrancy, oracle manipulation, proxy exploits
- **Prática:** reproduzir 2 hacks famosos em ambiente de testes
- **Ferramentas:** Foundry, Slither, Mythril, Tenderly
- **Tempo:** 30h

### Módulo 17 — Threat Intelligence e OSINT Avançado
- **Objetivo:** cruzar dados on-chain com OSINT tradicional
- **Conteúdo:** identificação por metadados, redes sociais, dark web monitoring, correlação de ataques
- **Prática:** investigação completa atribuindo identidade a endereço anônimo
- **Ferramentas:** Maltego, Recon-ng, Nansen, Arkham Ultra
- **Tempo:** 25h

**Total trilha avançada: ~145h (4-6 meses)**

---

## Plano Alternativo: Programa Intensivo de 3 Meses

Para quem tem 15-20h/semana disponíveis:

**Mês 1 — Fundamentos (60h)**
- Módulos 1-5: blockchain, explorers, UTXO, account, multi-chain

**Mês 2 — Rastreamento Avançado (60h)**
- Módulos 6-11: DeFi, padrões, cross-chain, mixers, contratos, golpes

**Mês 3 — Forense Aplicada (60h)**
- Módulos 12-14: ferramentas institucionais, casos end-to-end, persecução BR

---

## Cursos e Certificações

| Curso | Instituição | Foco |
|---|---|---|
| Chainalysis Certified Investigator | Chainalysis | Rastreamento profissional (gratuito para LE) |
| CTCE (Certified Cryptocurrency Trainer) | Chainalysis | Certificação avançada |
| TRM Academy | TRM Labs | Forense e compliance |
| Elliptic Academy | Elliptic | Compliance + investigação |
| Crypto Investigator Program | Blockchain Intelligence Group | Forense policial |
| Blockchain Council | Diversos | Certificações variadas |
| Cyfrin Updraft | Cyfrin | Auditoria de smart contracts (gratuito) |
| Secureum | Secureum | Segurança EVM (open-source) |

## Livros Essenciais

1. **"Mastering Bitcoin"** — Andreas Antonopoulos (fundamentos)
2. **"Mastering Ethereum"** — Antonopoulos + Gavin Wood (fundamentos EVM)
3. **"Tracers in the Dark"** — Andy Greenberg (casos reais de investigação cripto)
4. **"The Infinite Machine"** — Camila Russo (história Ethereum)
5. **"Digital Gold"** — Nathaniel Popper (história Bitcoin)
6. **"Crypto Anti-Money Laundering"** — vários autores (operacional AML)

## Comunidades para Networking

- **r/BitcoinCrimes** (Reddit)
- **Chainalysis Customer Community** (para licenciados)
- **Telegram grupos de OSINT e cibercrime** (privados, convite)
- **Conferências:** Consensus, DefCon Village, FINTELLIGENCE, Cryptocurrency Investigations Conference
- **Brasil:** GNCOC, ENCCLA, Congressos da Polícia Federal

## Dica Final

Teoria sem prática é inútil em investigação on-chain. Dedique **pelo menos 60% do tempo** a exercícios, análises de casos reais e simulações. Use o skill `/simulacao-investigacao` para praticar regularmente.

Acompanhe casos reais via **Rekt.news**, **SlowMist**, **PeckShield** e **Chainalysis Blog** — leia 1-2 casos por semana e reproduza a análise.
