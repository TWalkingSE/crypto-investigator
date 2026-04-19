# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/)
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [3.0.0] — 2026-04-19

### Adicionado
- Arquitetura completa baseada no padrão **Agent Skills** (cross-IDE)
- `AGENTS.md` universal — identidade, guardrails e regras canônicas
- `CLAUDE.md`, `.cursorrules`, `.windsurf/rules/` e `.github/copilot-instructions.md` para compatibilidade cross-IDE
- 12 agent skills especializados em `.github/skills/`:
  - `blockchain-id` — protocolo obrigatório para endereços 0x
  - `utxo-tracing` — rastreamento em Bitcoin e similares
  - `account-tracing` — rastreamento em Ethereum/EVM e account-based
  - `cross-chain-tracing` — investigação multi-hop, bridges, DeFi, mixers
  - `smart-contract-audit` — análise de contratos e red flags
  - `scam-patterns` — 12 tipologias de golpe em cripto
  - `persecucao-patrimonial` — busca, apreensão e destinação (Brasil)
  - `simulacao-investigacao` — cenários de prática com gabarito
  - `investigation-report` — template de relatório investigativo
  - `on-chain-patterns` — catálogo de padrões comportamentais
  - `crypto-tools-kb` — base de conhecimento indexada de ferramentas
  - `roteiro-estudo` — plano de capacitação por nível
- Base de conhecimento com 10 arquivos de referência em `.github/skills/crypto-tools-kb/references/`:
  - Explorers, análise de carteiras, forense institucional, visualização, contratos e scam, DEX/DeFi, NFT, CLI/open-source, bases de maliciosos, ferramentas brasileiras
- Wrappers de descoberta em `.claude/skills/` e `.windsurf/skills/` apontando para skills canônicos
- Prompt interativo em `.github/prompts/crypto-investigator-menu.prompt.md`
- Templates de issue e pull request
- Documentos de governança: CONTRIBUTING, CODE_OF_CONDUCT (Contributor Covenant 2.1), SECURITY, LICENSE (MIT)

### Características
- **Carregamento progressivo**: always-on (~150 linhas) + skills sob demanda (~60-280L cada) + referências (~100-260L cada)
- **Framework: UTXO vs Account** diferenciação explícita em todas as análises
- **Protocolo 0x**: identificação obrigatória de blockchain antes de análise em endereços EVM
- **Separação FATO vs INFERÊNCIA** em todos os relatórios
- **Foco Brasil**: persecução patrimonial com Lei 14.478/2022, IN RFB 1.888/2019, Resolução BCB 314/2023

### Compatibilidade
- VS Code + GitHub Copilot
- Google Antigravity
- Windsurf (Cascade)
- Cursor
- Claude Code
- GitHub Copilot CLI
- Kiro
- Outros agentes compatíveis com a especificação Agent Skills

---

## Futuras Versões (roadmap)

### [3.1.0] — planejado
- Skill `/malware-crypto` para análise de malware específico de cripto
- Skill `/defi-exploits` especializado em exploits de protocolos
- Expansão da base de conhecimento com fontes específicas de Solana e Tron
- Integração com fontes públicas atualizadas de endereços sancionados

### [3.2.0] — planejado
- Templates adicionais de peças jurídicas (minutas de busca, requisição, relatório)
- Cenários de simulação adicionais (Monero forense, Ordinals Bitcoin, hacks recentes)
