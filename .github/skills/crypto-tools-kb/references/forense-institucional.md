# Ferramentas Forenses Institucionais

Ferramentas profissionais com licença paga, usadas por polícias, agências de inteligência, compliance de exchanges e empresas de investigação. Oferecem maior profundidade de rastreamento, auditoria e aceitação processual.

## Top Tier (Institucional)

| Ferramenta | Empresa | Especialidade | Acesso |
|---|---|---|---|
| Chainalysis Reactor | Chainalysis | Rastreamento forense end-to-end | Licença institucional |
| Chainalysis KYT | Chainalysis | Monitoramento de risco em tempo real para exchanges | Licença |
| TRM Labs | TRM | Forense, compliance, triagem | Licença institucional |
| Elliptic Investigator | Elliptic | Investigação e compliance | Licença |
| Crystal Blockchain | Bitfury | Análise de fluxo, pontuação de risco | Licença |
| CipherTrace | Mastercard | Forense + compliance | Licença |
| Scorechain | Scorechain | AML + investigação | Licença |
| Coinfirm | Coinfirm | Due diligence on-chain | Licença |
| Merkle Science | Merkle Science | Detecção preditiva de risco | Licença |
| AnChain.AI | AnChain | Threat intelligence on-chain | Licença |

## Especializadas

| Ferramenta | Especialidade | URL |
|---|---|---|
| Chainabuse | Denúncias comunitárias (parceria Chainalysis) | chainabuse.com |
| Blockchain Intelligence Group (QLUE) | Forense policial | blockchaingroup.io |
| Cielo Finance | Intelligence em carteiras | cielo.finance |
| BlockSci | Framework acadêmico de análise | github.com/citp/BlockSci |
| GraphSense | Framework open-source (TU Wien) | graphsense.info |

## Capacidades Típicas

Ferramentas top tier oferecem:

- **Attribution**: identifica a entidade por trás de um endereço (exchange, serviço, mixer, golpista conhecido)
- **Clustering**: agrupa endereços da mesma entidade via heurísticas proprietárias
- **Risk scoring**: pontua endereço/transação (0-100) baseado em conexões
- **Tracing visual**: grafo interativo de fluxo
- **Monitoring**: alerta em tempo real sobre movimentações
- **Compliance**: screening contra sanções, KYC
- **Case management**: organização de investigações, colaboração em equipe
- **Court-ready reports**: relatórios padronizados para uso judicial

## Como Acessar (para agentes públicos brasileiros)

- **Parcerias governamentais**: algumas ferramentas fornecem licenças para law enforcement via convênios
- **Capacitação**: Chainalysis, TRM e Elliptic oferecem treinamentos específicos para polícia
- **Contato via compliance de exchanges**: exchanges brasileiras frequentemente têm contratos com estas plataformas e podem compartilhar análises em cooperação formal
- **Convênio com Receita Federal / COAF**: órgãos brasileiros já utilizam algumas dessas ferramentas

## Quando Recomendar ao Investigador

Use estas ferramentas quando:

- Caso tem implicação processual direta (necessidade de relatório técnico auditável)
- Valor envolvido é significativo
- Há necessidade de confirmar atribuição (quem é o dono do endereço)
- Investigação multi-chain complexa
- Caso conecta com sanções internacionais ou organizações criminosas

Para casos simples de triagem, ferramentas gratuitas (Etherscan + Arkham + Breadcrumbs) geralmente são suficientes.

## Limitações

Mesmo ferramentas institucionais têm limites:

- **Privacy coins** (Monero): rastreamento quase inviável
- **Mixers recentes**: capacidade de deanonimização varia
- **Protocolos novos**: pode haver delay de cobertura
- **Atribuição**: sempre probabilística — nunca 100%
- **Dependência de labels**: se a entidade não está no banco, não é identificada
