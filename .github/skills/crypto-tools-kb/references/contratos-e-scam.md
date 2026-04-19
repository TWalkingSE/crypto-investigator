# Análise de Smart Contracts e Detecção de Scam

Ferramentas para identificar tokens maliciosos, honeypots, rug pulls em potencial, contratos com backdoors e riscos em protocolos DeFi.

## Scanners de Token (Automatizados)

| Ferramenta | O que faz | URL | Custo |
|---|---|---|---|
| Token Sniffer | Detecção de scams em tokens ERC-20/BEP-20 | tokensniffer.com | Gratuito |
| De.Fi Scanner | Auditoria automatizada multi-chain | de.fi/scanner | Gratuito |
| GoPlusLabs | API de segurança para tokens | gopluslabs.io | Gratuito (API) |
| Honeypot.is | Verifica se token é honeypot | honeypot.is | Gratuito |
| StaySAFU | Scanner de rug pull | staysafu.org | Gratuito |
| RugDoc | Auditoria de farms e pools | rugdoc.io | Gratuito |
| QuickIntel | Intelligence de token | quickintel.io | Freemium |
| Dextools Audit | Auditoria rápida | dextools.io | Freemium |

## Auditoria Profunda

| Ferramenta | O que faz | URL | Custo |
|---|---|---|---|
| CertiK Skynet | Monitoramento contínuo de contratos | skynet.certik.com | Freemium |
| PeckShield | Auditoria profissional | peckshield.com | Serviço pago |
| Trail of Bits | Auditoria profissional | trailofbits.com | Serviço pago |
| OpenZeppelin Defender | Monitoramento + resposta | defender.openzeppelin.com | Pago |
| Forta Network | Detecção em tempo real de exploits | forta.network | Gratuito para queries |

## Análise Estática e Simbólica (CLI / Open-Source)

| Ferramenta | Linguagem | URL |
|---|---|---|
| Slither | Solidity (análise estática) | github.com/crytic/slither |
| Mythril | EVM (execução simbólica) | github.com/ConsenSys/mythril |
| Echidna | Fuzzing de contratos | github.com/crytic/echidna |
| Manticore | Execução simbólica | github.com/trailofbits/manticore |
| Aderyn | Rust-based static analyzer | github.com/Cyfrin/aderyn |
| Smartbugs | Framework de avaliação | github.com/smartbugs/smartbugs |

## Decompiladores (para contratos não verificados)

Quando o contrato não tem código-fonte verificado no Etherscan, é possível decompilar o bytecode:

| Ferramenta | URL |
|---|---|
| Dedaub (EVM Decompiler) | library.dedaub.com |
| Panoramix | github.com/palkeo/panoramix |
| Etherscan "Decompile" | Aba Contract → Decompile bytecode |
| EthervmIO | ethervm.io/decompile |

## Análise de Transação (Decodificação)

Para entender o que aconteceu dentro de uma TX complexa:

| Ferramenta | O que faz | URL |
|---|---|---|
| Phalcon (BlockSec) | Debugger visual de TX | phalcon.blocksec.com |
| Tenderly | Debugger + simulation | tenderly.co |
| Etherscan TX Details | "State Changes" + "Logs" | etherscan.io |
| ethtx.info | Decodificação com labels | ethtx.info |
| Sentio | Analytics profundo de TX | sentio.xyz |

## Verificação de Aprovações (Approvals)

Ferramentas para ver e revogar aprovações de token:

| Ferramenta | Redes | URL |
|---|---|---|
| Revoke.cash | Multi-chain EVM | revoke.cash |
| Etherscan Token Approvals | Ethereum | etherscan.io/tokenapprovalchecker |
| BscScan Token Approvals | BSC | bscscan.com/tokenapprovalchecker |
| Unrekt | Multi-chain | unrekt.net |

## MEV e Exploits

| Ferramenta | O que faz | URL |
|---|---|---|
| MEV-Explore (Flashbots) | Histórico de MEV | mev-explore.flashbots.net |
| EigenPhi | Analytics de MEV por endereço | eigenphi.io |
| Phalcon Explorer | TX explorer especializado | phalcon.xyz |
| Rekt News | Histórico de hacks e exploits | rekt.news |
| DefiYield REKT Database | Base de hacks DeFi | defiyield.app/rekt-database |

## Fluxo de Análise Recomendado

1. **Triagem rápida**: Token Sniffer + Honeypot.is (2 minutos)
2. **Análise de liquidez**: DexScreener para ver pool, liquidez, holders
3. **Análise de contrato**: se código verificado, inspecionar no Etherscan; se não, Dedaub Decompiler
4. **Análise de padrões**: verificar deployer do contrato em histórico (outros tokens criados?)
5. **Simulação** (se necessário): Tenderly para simular uma venda antes de executar
6. **Cruzamento**: Chainabuse + Scam Sniffer para ver denúncias

## Red Flags Rápidos em Token

| Flag | Severidade |
|---|---|
| Código não verificado | ALTA |
| LP não lockado | ALTA |
| Owner não renunciou | MÉDIA (depende do código) |
| Concentração de tokens em poucas carteiras | ALTA |
| Contrato criado há menos de 7 dias | MÉDIA |
| Muito marketing em redes, sem código auditado | ALTA |
| Fee de venda muito maior que de compra | CRÍTICA (honeypot) |
| Deployer criou múltiplos tokens antes (rug serial) | ALTA |
