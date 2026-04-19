---
name: scam-patterns
description: >
  Identificação, classificação e investigação de golpes e esquemas fraudulentos 
  em criptoativos. Use para: rug pull, ponzi, esquema em pirâmide, phishing, 
  SIM swap com roubo de cripto, romance scam (pig butchering), fake airdrop, 
  ransomware em cripto, address poisoning, clipboard hijacking, NFT wash 
  trading, fake ICO/presale, exit scam de exchange, honeypot tokens. Cada 
  golpe tem padrão on-chain específico que este skill ensina a reconhecer 
  e investigar.
---

# Golpes e Esquemas Fraudulentos — Padrões de Investigação

## Catálogo de Golpes

### 1. Rug Pull

**Padrão on-chain:**
- Liquidez removida abruptamente pelo deployer do token
- Dev wallet recebe grande quantidade de ETH/BNB no momento da remoção
- Token passa a não poder ser vendido (preço despenca)

**Como investigar:**
1. Identificar endereço do deployer (criador do contrato)
2. Verificar TX de remoção de liquidez no pool DEX
3. Rastrear para onde foram os fundos após a remoção (skill `/account-tracing`)
4. Analisar o contrato (skill `/smart-contract-audit`) — frequentemente tem backdoors
5. Documentar timestamp da remoção vs. início do projeto

**Red flags preventivos:**
- LP tokens NÃO lockados
- Concentração de tokens em poucas carteiras
- Contrato não verificado
- Equipe anônima sem auditoria
- Marketing agressivo em redes sociais

### 2. Ponzi / Pirâmide

**Padrão on-chain:**
- Pagamentos a investidores antigos vêm de novos depósitos
- Carteira central concentra fundos
- Colapso quando entradas diminuem

**Como investigar:**
1. Mapear fluxo de depósitos vs. saques ao longo do tempo
2. Identificar carteira central que recebe e redistribui
3. Verificar se existe atividade econômica real por trás (geralmente não)
4. Rastrear saída de fundos quando os operadores "vão embora"

**Exemplos notórios:** PlusToken (2019, ~$2B), Forsage (esquema em pirâmide MLM on-chain), BitConnect.

### 3. Phishing Web3

**Padrão on-chain:**
- Vítima assina `approve()` ou `permit()` para contrato malicioso
- Em seguida, contrato drena tokens via `transferFrom()`
- Frequentemente usa tokens ERC-20 e NFTs

**Como investigar:**
1. No endereço da vítima, verificar aprovações recentes (revoke.cash)
2. Identificar contrato malicioso que recebeu approve
3. Rastrear saque: contrato → endereço do golpista → mixer ou exchange
4. Verificar se há outras vítimas com o mesmo contrato malicioso (busca no Etherscan)

**Dicas de identificação:**
- Site falso (URL similar: metarnask.io, opnsea.io, etc.)
- Airdrops falsos exigindo "ativação" via aprovação
- E-mails phishing sobre "atualização de segurança" da carteira

### 4. SIM Swap + Roubo

**Padrão on-chain:**
- Fundos movidos rapidamente após comprometimento
- Geralmente madrugada (horário de sono da vítima)
- Múltiplas carteiras intermediárias em curto tempo
- Destino final: exchanges com KYC ou P2P

**Como investigar:**
1. Rastrear movimentação a partir do endereço da vítima
2. Identificar exchanges de saída
3. Correlacionar com logs de operadora telefônica (quando houve o swap)
4. Dados da conta da exchange (KYC) para identificação

### 5. Romance Scam / Pig Butchering

**Padrão on-chain:**
- Depósitos graduais da vítima em plataforma falsa (fake exchange/DEX)
- Endereço da plataforma recebe de múltiplas vítimas
- Operador consolida e saca para exchange real ou P2P
- Volumes altos, TX frequentes

**Como investigar:**
1. Identificar endereço de depósito da plataforma falsa
2. Analisar padrão (muitas entradas, poucos saques grandes)
3. Rastrear saques para exchange/P2P
4. Coordenar com vítimas (múltiplos casos frequentemente apontam para mesma infra)
5. Registrar URL da plataforma falsa para histórico

**Scale:** Pig butchering é hoje o maior crime de cripto por volume — bilhões por ano. Frequentemente opera a partir de sudeste asiático em operações de tráfico humano.

### 6. Fake Airdrop / Dusting Attack

**Padrão on-chain:**
- Token aparece na carteira sem solicitação
- Valor irrisório (dust) ou nome sugestivo
- Interação com contrato do token (para reivindicar "airdrop") drena a carteira

**Como investigar:**
1. Analisar contrato do token recebido (skill `/smart-contract-audit`)
2. Verificar site oficial do token (geralmente clone de site real)
3. Alertar vítima para NÃO interagir
4. Rastrear endereço distribuidor — geralmente envia para milhares

### 7. Ransomware

**Padrão on-chain:**
- Pagamento em BTC ou XMR para endereço fornecido na nota de resgate
- Fragmentação e movimentação para mixer
- Destino final: exchanges que listam Monero ou P2P

**Como investigar:**
1. Registrar endereço de pagamento da nota
2. Rastrear movimentação (skill `/utxo-tracing` para BTC)
3. Cruzar com bases de ransomware conhecidos:
   - Chainalysis sanctions
   - Ransomwhere.re
   - ID Ransomware
4. Se passou por mixer: foco em pontos de entrada/saída
5. Cooperar com law enforcement internacional

**Grupos ativos:** LockBit, BlackCat/ALPHV, Cl0p, Play, Conti (extinto).

### 8. Address Poisoning

**Padrão on-chain:**
- TX de valor zero ou ínfimo de endereço similar ao da vítima
- Objetivo: vítima copia o endereço errado do histórico ao fazer pagamento futuro

**Como investigar:**
1. Verificar histórico — entrada anômala de valor ~zero
2. Comparar endereços: similares visualmente (prefixo/sufixo igual)
3. Alertar vítima antes de nova transação
4. Rastrear endereço falso (pode ter múltiplas vítimas)

### 9. NFT Wash Trading

**Padrão on-chain:**
- Compra-venda inflacionada de NFT entre carteiras do mesmo controlador
- Volume artificial para enganar compradores
- Frequente em coleções novas e marketplaces com incentivos (tokens de recompensa)

**Como investigar:**
1. No explorer ou em NFTScan, listar histórico de transferências
2. Verificar se compradores e vendedores têm relação (financiamento comum)
3. Analisar timing (compras e vendas muito próximas)
4. Comparar preços com o "floor" da coleção

### 10. Exit Scam de Exchange

**Padrão on-chain:**
- Exchange para de processar saques
- Grandes movimentações de hot/cold wallets para endereços desconhecidos
- Fundos passam por mixer ou privacy coin rapidamente

**Como investigar:**
1. Identificar carteiras principais da exchange
2. Monitorar movimentações anormais
3. Rastrear para onde vão os fundos
4. Coordenar com autoridades e outros investigadores afetados

**Exemplos históricos:** FTX (2022), QuadrigaCX (2019), Mt. Gox (2014), BitConnect.

### 11. Clipboard Hijacking / Malware

**Padrão on-chain:**
- Usuário copia endereço de destino; malware substitui pelo endereço do atacante
- TX envia para endereço errado
- Vítima só percebe após confirmação

**Como investigar:**
1. Analisar dispositivo da vítima (malware forensics)
2. Rastrear endereço que recebeu (provavelmente tem múltiplas vítimas)
3. Alertar comunidade sobre malware ativo
4. Ferramentas anti-malware: Malwarebytes, Kaspersky

### 12. Fake ICO / Presale

**Padrão on-chain:**
- Endereço recebe depósitos de muitos investidores
- Nunca entrega tokens prometidos OU entrega tokens sem valor
- Carteira do "projeto" saca para exchange ou mixer

**Como investigar:**
1. Endereço de recepção da ICO
2. Quantos depositaram, quanto total arrecadado
3. Site do projeto — existe, tem atividade?
4. Equipe é real ou fake? (Verificar LinkedIn, GitHub)
5. Rastrear saída dos fundos

## Bases de Dados de Endereços Fraudulentos

| Base | Especialidade | URL |
|---|---|---|
| **Chainabuse** | Denúncias de fraude multi-chain | chainabuse.com |
| **Scam Sniffer** | Detecção de phishing Web3 em tempo real | scamsniffer.io |
| **CryptoScamDB** | Base de scams conhecidos | cryptoscamdb.org |
| **OFAC SDN List** | Endereços sancionados pelo governo dos EUA | home.treasury.gov/policy-issues/financial-sanctions |
| **Ransomwhere** | Endereços de pagamento de ransomware | ransomwhere.re |
| **Etherscan Labels** | Labels públicos de endereços maliciosos | etherscan.io |
| **Bitcoin Abuse** | Endereços BTC reportados | bitcoinabuse.com |
| **Scam Alert (GoPlus)** | API de verificação | gopluslabs.io |

## Orientação ao Investigador

Ao receber um caso, pergunte:

1. **Tipo do golpe** (se já identificado) ou descrição do modus operandi
2. **Endereço(s) envolvido(s)**: vítima, suspeito, plataforma
3. **Blockchain** (se endereço 0x → `/blockchain-id`)
4. **Valores e timestamps**
5. **Documentação disponível**: prints de site falso, mensagens, e-mails
6. **Outras vítimas conhecidas** (caso investigativo coordenado)

## Integração com outros skills

- Analisar contrato associado ao golpe: `/smart-contract-audit`
- Rastrear saída dos fundos: `/account-tracing` ou `/utxo-tracing`
- Cross-chain (frequentemente usado para ofuscar): `/cross-chain-tracing`
- Padrões comportamentais associados: `/on-chain-patterns`
- Persecução no Brasil: `/persecucao-patrimonial`
- Gerar relatório: `/investigation-report`
