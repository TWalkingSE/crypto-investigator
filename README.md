# Crypto Investigator — Sistema de Investigação Forense em Criptoativos

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![AGENTS.md](https://img.shields.io/badge/AGENTS.md-compatible-blue)
![Agent Skills](https://img.shields.io/badge/Agent%20Skills-12-7c3aed)
![Knowledge Base](https://img.shields.io/badge/KB-10%20refer%C3%AAncias-0ea5e9)
![Idioma](https://img.shields.io/badge/Idioma-PT--BR-009c3b)

> Instruções, skills e base de conhecimento que transformam qualquer IDE com modo agente em um sistema de investigação forense especializado em rastreamento on-chain, análise de fluxo de fundos e inteligência patrimonial em criptoativos.

## O que é

O Crypto Investigator é um conjunto de **custom instructions**, **agent skills** e uma **base de conhecimento** que configuram LLMs em IDEs agentic para atuar como **orientador investigativo** em casos envolvendo criptoativos.

Ele não acessa blockchains diretamente — o valor está em **ensinar o investigador** a encontrar, interpretar e conectar dados on-chain usando as ferramentas corretas, e em **analisar** os dados que o investigador trouxer dos explorers.

### Princípios centrais

- **Rastreabilidade é prioridade** — toda análise contribui para responder "para onde foi o dinheiro?"
- **Identifique a blockchain antes de analisar** — endereços `0x` existem em dezenas de redes EVM, erro fatal é assumir Ethereum sem verificar
- **UTXO ≠ Account** — diferencia explicitamente Bitcoin (UTXO) de Ethereum (account-based); o modelo muda tudo na técnica de rastreamento
- **Fato vs Inferência** — separação rigorosa entre dados observados e interpretações
- **Proporcionalidade e legalidade** — orientação sempre dentro do arcabouço legal brasileiro e internacional
- **Cadeia de custódia** — toda apreensão ou movimentação documentada para aceitação processual

### O que está incluso

- **12 agent skills** com instruções detalhadas para tarefas especializadas
- **Base de conhecimento** com 10 arquivos temáticos e 100+ ferramentas catalogadas
- **60+ padrões comportamentais** on-chain documentados
- **12 tipologias de golpe** em criptoativos com padrões investigativos
- **Cenários de simulação** para prática guiada
- **Fluxo de persecução patrimonial** no contexto brasileiro (Lei 14.478/2022, IN RFB 1.888/2019)
- **Formato universal** — funciona com qualquer LLM (Claude, GPT, Gemini, etc.)

## IDEs e ferramentas compatíveis

O projeto usa o padrão aberto `AGENTS.md` + `SKILL.md`, reconhecido nativamente por:

| IDE / Ferramenta | Arquivo de regras | Skills | Status |
| --- | --- | --- | --- |
| **VS Code + GitHub Copilot** | `AGENTS.md` + `.github/copilot-instructions.md` | `.github/skills/` | ✅ Completo |
| **Google Antigravity** | `AGENTS.md` | `.github/skills/` | ✅ Completo |
| **Windsurf (Cascade)** | `AGENTS.md` + `.windsurf/rules/` | `.github/skills/` e `.windsurf/skills/` | ✅ Completo |
| **Cursor** | `AGENTS.md` + `.cursorrules` | `.github/skills/` | ✅ Completo |
| **Claude Code** | `CLAUDE.md` + `AGENTS.md` | `.github/skills/` e `.claude/skills/` | ✅ Completo |
| **GitHub Copilot CLI** | `AGENTS.md` | `.github/skills/` | ✅ Completo |
| **Kiro** | `AGENTS.md` | `.github/skills/` | ✅ Compatível |

> Todas essas IDEs são forks do VS Code ou compatíveis com a especificação Agent Skills. Extensões, atalhos e temas funcionam normalmente.

## Como usar

1. Clone ou baixe este repositório
2. Abra a pasta na sua IDE com modo agente ativo
3. A IDE carrega automaticamente o `AGENTS.md` e as instruções
4. Faça perguntas sobre investigação em cripto no chat do agente

### Exemplos de perguntas

```
Preciso rastrear esse endereço: 0x742d35Cc6634C0532925a3b844Bc9e7595f2bD18
Rastrear Bitcoin sacado da Binance para bc1q...
Analisar o contrato desse token suspeito
Como funciona rastreamento cross-chain?
Analise meu caso de suspeita de rug pull
Quais ferramentas uso para investigar USDT na Tron?
Quero praticar um cenário de pig butchering
Como proceder com busca e apreensão de cripto no Brasil?
Monte um roteiro de estudo para mim
```

### Skills disponíveis

Para usar um skill específico, digite `/nome-do-skill` no chat:

| Comando | O que faz |
| --- | --- |
| `/blockchain-id` | Protocolo de identificação de blockchain (obrigatório para endereços 0x) |
| `/utxo-tracing` | Rastreamento em Bitcoin, Litecoin, Dogecoin e similares |
| `/account-tracing` | Rastreamento em Ethereum, EVM, Solana, Tron, Ripple, etc. |
| `/cross-chain-tracing` | Investigação multi-hop: bridges, DEX, DeFi, mixers |
| `/smart-contract-audit` | Análise de contratos inteligentes e red flags |
| `/scam-patterns` | 12 tipologias de golpe com padrões investigativos |
| `/persecucao-patrimonial` | Busca, apreensão, custódia e destinação (Brasil) |
| `/simulacao-investigacao` | Cenários práticos com gabarito |
| `/investigation-report` | Template de relatório investigativo |
| `/on-chain-patterns` | Catálogo de padrões comportamentais on-chain |
| `/crypto-tools-kb` | Base de conhecimento com 100+ ferramentas |
| `/roteiro-estudo` | Plano de capacitação personalizado |

## Estrutura do projeto

```
crypto-investigator/
├── README.md
├── LICENSE                                # Licença MIT
├── CHANGELOG.md                           # Histórico de versões
├── CONTRIBUTING.md                        # Guia de contribuição
├── CODE_OF_CONDUCT.md                     # Contributor Covenant 2.1
├── SECURITY.md                            # Política de segurança
├── .gitignore
├── AGENTS.md                              # Identidade e regras (universal)
├── CLAUDE.md                              # Ajustes específicos para Claude
├── .cursorrules                           # Regras para Cursor
├── .github/
│   ├── copilot-instructions.md
│   ├── ISSUE_TEMPLATE/                    # Templates (bug, ferramenta, skill)
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── prompts/
│   │   └── crypto-investigator-menu.prompt.md
│   └── skills/                            # 12 skills canônicos
│       ├── account-tracing/
│       │   └── SKILL.md
│       ├── blockchain-id/
│       │   └── SKILL.md
│       ├── cross-chain-tracing/
│       │   └── SKILL.md
│       ├── crypto-tools-kb/
│       │   ├── SKILL.md
│       │   └── references/                # 10 arquivos de referência
│       │       ├── analise-carteiras.md
│       │       ├── bases-maliciosos.md
│       │       ├── brasil.md
│       │       ├── cli-open-source.md
│       │       ├── contratos-e-scam.md
│       │       ├── dex-defi.md
│       │       ├── explorers-blockchain.md
│       │       ├── forense-institucional.md
│       │       ├── nft.md
│       │       └── visualizacao-fluxo.md
│       ├── investigation-report/SKILL.md
│       ├── on-chain-patterns/SKILL.md
│       ├── persecucao-patrimonial/SKILL.md
│       ├── roteiro-estudo/SKILL.md
│       ├── scam-patterns/SKILL.md
│       ├── simulacao-investigacao/SKILL.md
│       ├── smart-contract-audit/SKILL.md
│       └── utxo-tracing/SKILL.md
├── .windsurf/                             # Compatibilidade Cascade
│   ├── rules/
│   │   └── crypto-investigator.md
│   └── skills/                            # 12 wrappers
└── .claude/                               # Compatibilidade Claude Code
    └── skills/                            # 12 wrappers
```

> Os diretórios `.windsurf/skills/` e `.claude/skills/` contêm apenas **wrappers
> de descoberta** (frontmatter `name`/`description` + ponteiro para o arquivo
> canônico). O conteúdo real dos skills vive em `.github/skills/`, evitando
> duplicação e drift de informação.

## Carregamento progressivo

O projeto não joga centenas de linhas no contexto de uma vez. Usa três níveis:

| Nível | O que carrega | Quando | Tamanho |
| --- | --- | --- | --- |
| **Always-on** | `AGENTS.md` + instruções da IDE | Toda conversa | ~160 linhas |
| **Sob demanda** | Skills (`SKILL.md`) | Quando o tema é relevante | ~60-280 linhas cada |
| **Referência** | Arquivos em `references/` | Quando o skill consulta dados | ~100-260 linhas cada |

Uma pergunta sobre rastreamento Bitcoin carrega ~160L (always-on) + ~110L (`/utxo-tracing`) = **~270 linhas** de contexto, em vez de todo o conhecimento do projeto.

## Framework UTXO vs Account

A distinção é **central** para qualquer rastreamento:

| Aspecto | UTXO (Bitcoin, Litecoin) | Account (Ethereum, EVM) |
| --- | --- | --- |
| **Conceito** | Transação consome "moedas" antigas e cria novas | Conta com saldo — débito e crédito direto |
| **Analogia** | Pagar com cédulas e receber troco | Transferência bancária entre contas |
| **Endereços por carteira** | Múltiplos (um novo por transação é comum) | Geralmente um único endereço principal |
| **Tokens** | Não nativo (Omni/Counterparty — obsoletos) | Nativo — ERC-20, BEP-20, SPL, TRC-20 |
| **Smart contracts** | Limitados | Complexos — DeFi, NFT, bridges tudo em contratos |
| **Ferramenta chave** | OXT.me, WalletExplorer | Etherscan, Arkham, DeBank |

## Protocolo do 0x

Endereços começando com `0x` existem em **dezenas de blockchains simultaneamente** (Ethereum, BSC, Polygon, Arbitrum, Base, Optimism, Avalanche, etc.). Cada rede pode ter saldos e transações completamente diferentes.

**Erro fatal é assumir Ethereum sem verificar.** Por isso o skill `/blockchain-id` é obrigatório antes de qualquer análise em endereço 0x.

## Contexto Brasileiro

O projeto tem foco específico em investigação no Brasil, incluindo:

- **Lei 14.478/2022** — Marco Legal dos Criptoativos
- **IN RFB 1.888/2019** — Declaração obrigatória de operações
- **Resolução BCB 314/2023** — Regulamentação de VASPs
- **Lei 9.613/1998** — Lavagem e alienação antecipada
- **Enunciados 162 e 209 CJF** — Persecução patrimonial de ativos digitais
- **Sisbajud** — integração com exchanges brasileiras
- **COAF / Receita Federal / MJ-DRCI** — canais de cooperação
- **Convenção de Budapeste** — cooperação internacional em cibercrime

## Limitações importantes

- **Não acessa blockchains em tempo real** — depende de dados coletados pelo investigador
- **Não fornece assessoria jurídica** para casos concretos — contextualiza como educacional
- **Não fornece assessoria financeira** — nunca recomenda comprar, vender ou investir
- **Não inventa jurisprudência** — cita apenas o que existe com certeza
- **Não garante anonimato absoluto** em rastreamentos que envolvem Monero, mixers ou protocolos de privacidade — sinaliza limites
- Resultados devem ser **validados com ferramentas profissionais** (Chainalysis, TRM, Elliptic, Arkham) antes de uso processual

## Fonte primária

Base de conhecimento construída a partir de:

- System prompt original do Crypto Investigator (TWalking, 2025-2026)
- [Chainalysis Blog & Reports](https://www.chainalysis.com/blog/)
- [TRM Labs Insights](https://www.trmlabs.com/resources)
- [Elliptic Insights](https://www.elliptic.co/resources)
- [SlowMist Incidents](https://hacked.slowmist.io/)
- [Rekt News](https://rekt.news/)
- Legislação brasileira (planalto.gov.br)
- Documentação oficial das ferramentas catalogadas
- Casos documentados publicamente

## Contribuindo

Contribuições são bem-vindas. Ver [CONTRIBUTING.md](CONTRIBUTING.md) para detalhes.

Ao sugerir uma ferramenta, inclua: nome, link oficial, open-source (Sim/Não), chains suportadas, custo, diferencial e alertas de incidentes (se houver).

## Código de Conduta

Este projeto adota o [Contributor Covenant 2.1](CODE_OF_CONDUCT.md).

## Segurança

Ver [SECURITY.md](SECURITY.md) para política de reporte e boas práticas no uso em investigações reais.

## Licença

[MIT](LICENSE)

---

⚠️ **Aviso:** Este projeto é destinado a profissionais de investigação criminal, perícia digital, Ministério Público, Poder Judiciário, advocacia, compliance e pesquisa acadêmica. O uso deve respeitar LGPD, Marco Civil da Internet e toda legislação aplicável. Orientações são educacionais e devem ser validadas por profissionais qualificados em casos concretos.

⚖️ **Não constitui assessoria jurídica ou financeira.**

🕵️ *"Para onde foi o dinheiro?" — a pergunta central de toda investigação on-chain.*
