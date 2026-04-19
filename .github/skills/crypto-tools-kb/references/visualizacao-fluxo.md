# Visualização de Fluxo de Fundos e Grafos

Ferramentas que transformam dados de transações em grafos visuais — essenciais para comunicar achados em relatórios e identificar padrões complexos.

## Visualização Interativa de Fluxo

| Ferramenta | Chains | URL | Custo |
|---|---|---|---|
| Breadcrumbs | Multi-chain EVM + BTC | breadcrumbs.app | Freemium (limite grátis, premium ilimitado) |
| Metasleuth (BlockSec) | Multi-chain | metasleuth.io | Freemium |
| Misttrack (SlowMist) | Multi-chain | misttrack.io | Freemium — foco em fundos roubados |
| Arkham Visualizer | Multi-chain EVM | platform.arkham.intelligence | Gratuito com conta |
| Bubblemaps | Multi-chain | bubblemaps.io | Freemium |
| GraphSense | Multi-chain acadêmico | graphsense.info | Open-source |
| OXT.me | Bitcoin | oxt.me | Gratuito |
| Crystal Expert | Multi-chain | expert.crystalblockchain.com | Licença |

## Grafos de Relações (não-transação)

| Ferramenta | O que mostra | URL |
|---|---|---|
| Bubblemaps | Distribuição de holders e conexões | bubblemaps.io |
| Arkham Entity | Entidades ligadas via endereços conhecidos | arkham.com |
| Nansen Wallet Profiler | Carteiras relacionadas por padrão | nansen.ai |

## Análise Temporal

| Ferramenta | Especialidade | URL |
|---|---|---|
| Dune Analytics | Dashboards customizados SQL | dune.com |
| Nansen | Séries temporais profissionais | nansen.ai |
| Etherscan Analytics | Análise básica por endereço | etherscan.io (aba Analytics no endereço) |
| Flipside Crypto | Dashboards comunitários | flipsidecrypto.xyz |
| DefiLlama | DeFi temporal | defillama.com |

## Ferramentas de Desenho Customizado

Quando as ferramentas nativas não bastam, investigadores constroem grafos próprios:

| Ferramenta | Para que serve |
|---|---|
| **Maltego** | Link analysis profissional (com transforms para cripto) |
| **i2 Analyst's Notebook** | Grafo forense institucional (IBM) |
| **Gephi** | Visualização de grafos grandes (open-source) |
| **yEd** | Diagramas limpos para relatórios |
| **Neo4j + Bloom** | Banco de grafos + visualização |

## Boas Práticas de Visualização para Relatório

1. **Cores por tipo de endereço:**
   - Vermelho: alvo investigado
   - Amarelo: intermediário
   - Verde: exchange / ponto de identificação
   - Preto: mixer / ponto de opacidade

2. **Espessura da seta = valor:** proporcional ao volume movimentado

3. **Legenda temporal:** indicar timestamps em hops críticos

4. **Anotações:** marcar hops com padrões específicos (ex.: "PEELING CHAIN", "BRIDGE HOP")

5. **Evitar excesso:** grafos com 50+ nós se tornam ilegíveis — agrupe clusters ou faça múltiplos grafos

6. **Exportar para PDF vetorial:** evita perda de qualidade em laudos impressos

## Mapa Textual (Formato Preferido do Crypto Investigator)

Quando não for possível gerar grafo visual, o Crypto Investigator produz mapas textuais que capturam o essencial do fluxo em formato monospace. Ver `/investigation-report` e `/cross-chain-tracing` para exemplos.
