# Bases de Endereços Maliciosos e Sanções

Bases de dados públicas e comunitárias para verificar se um endereço está associado a crime, sanção ou denúncia.

## Sanções Oficiais

| Fonte | Jurisdição | URL | O que contém |
|---|---|---|---|
| OFAC SDN List | EUA | home.treasury.gov/policy-issues/financial-sanctions/specially-designated-nationals-and-blocked-persons-list | Endereços sancionados pelos EUA (Tornado Cash, Lazarus, Hydra) |
| OFAC Crypto Addresses | EUA | sanctionslist.ofac.treas.gov | Lista filtrada de endereços |
| UK OFSI | Reino Unido | gov.uk/government/publications/financial-sanctions-consolidated-list-of-targets | — |
| EU Sanctions | União Europeia | sanctionsmap.eu | — |
| Canada (OSFI) | Canadá | osfi-bsif.gc.ca | — |
| COAF / UIF | Brasil | coaf.fazenda.gov.br | Lista ONU + sanções específicas |

**Importante:** Endereços na OFAC SDN têm status de sancionados — transações com eles podem configurar violação de sanções. Tether e Circle geralmente congelam automaticamente.

## Bases Comunitárias de Fraude

| Base | Especialidade | URL |
|---|---|---|
| Chainabuse | Denúncias multi-chain (parceria Chainalysis) | chainabuse.com |
| Scam Sniffer | Phishing Web3 em tempo real | scamsniffer.io |
| CryptoScamDB | Scams conhecidos históricos | cryptoscamdb.org |
| Bitcoin Abuse | Endereços BTC reportados | bitcoinabuse.com |
| WhaleLend ScamDB | Scams em DeFi | whalelend.com |
| Bad Crypto | Denúncias comunitárias | badcrypto.com |

## Ransomware

| Base | URL |
|---|---|
| Ransomwhere.re | ransomwhere.re |
| ID Ransomware | id-ransomware.malwarehunterteam.com |
| Chainalysis Sanctions | chainalysis.com/free-crypto-sanctions-screening-tools |
| NoMoreRansom | nomoreransom.org |

## Threat Intelligence

| Fonte | Especialidade | URL |
|---|---|---|
| SlowMist Hacked | Hacks de cripto com endereços | hacked.slowmist.io |
| Rekt News | Retrospectivas de hacks | rekt.news |
| DeFi Yield REKT Database | Base de hacks DeFi | defiyield.app/rekt-database |
| CERT BR | Incidentes Brasil | cert.br |
| Krebs on Security | Blog de investigação | krebsonsecurity.com |
| MITRE ATT&CK | TTPs de APTs | attack.mitre.org |

## Darkweb e Leaks

| Fonte | Notas |
|---|---|
| OFAC (Hydra Market) | Endereços do market russo sancionado |
| Europol Operações | Relatórios públicos sobre apreensões |
| IRS-CI (EUA) | Relatórios anuais com endereços em casos públicos |

## APIs de Screening

Para verificação programática:

| Serviço | URL | Custo |
|---|---|---|
| Chainalysis Free Sanctions API | chainalysis.com/free-crypto-sanctions-screening-tools | Gratuito |
| TRM Labs API | trmlabs.com | Pago |
| Elliptic Navigator | elliptic.co | Pago |
| GoPlusLabs | gopluslabs.io | Freemium |
| Scam Sniffer API | scamsniffer.io | Freemium |

## Hot Wallets e Cold Wallets Conhecidas de Exchanges

Muitas ferramentas mantêm listas de endereços de hot wallets e cold wallets de exchanges:

| Fonte | URL |
|---|---|
| Etherscan "Exchange Wallet" label | etherscan.io/labelcloud (categoria Exchange) |
| Arkham Entities | platform.arkham.intelligence (filtro CEX) |
| WalletExplorer | walletexplorer.com (para Bitcoin) |
| Coinglass | coinglass.com/exchange-balance |

Importante: exchanges mudam endereços com frequência. Sempre cruzar com fonte atual.

## Identificação Preliminar

Ao encontrar um endereço suspeito, faça verificação rápida:

1. **Etherscan/BscScan Label** (se EVM) — verificar label público
2. **Arkham Intelligence** — entidade identificada?
3. **Chainabuse** — reportes comunitários?
4. **OFAC SDN** — sancionado?
5. **Scam Sniffer** — associado a phishing conhecido?
6. **WalletExplorer** (se BTC) — cluster identificado?

Se positivo em qualquer dessas bases, **sinalize ao investigador** e contextualize o achado no relatório.

## Procedimento Brasileiro

Em investigação no Brasil, adicionalmente:

- **COAF**: consultar LAC (Listagem de Advertência de Cumprimento) e listas ONU
- **Receita Federal**: cruzar CPF/CNPJ via IN 1.888/2019
- **Sisbajud**: verificar se há bloqueios já ativos
- **Banco Central**: consultar se há ação cautelar

Para cooperação internacional formal, via MLAT (autoridade central = Ministério da Justiça).
