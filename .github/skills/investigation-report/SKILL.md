---
name: investigation-report
description: >
  Gera relatório investigativo estruturado a partir de dados coletados pelo 
  investigador. Use ao finalizar qualquer análise completa de endereço, 
  transação ou caso de rastreamento. Produz documento formatado pronto para 
  incorporação em peça investigativa, laudo pericial, informação ao MP ou 
  apresentação em autos processuais. Separa fato observado de inferência, 
  indica nível de risco, ações prioritárias, ferramentas recomendadas e 
  limitações.
---

# Relatório Investigativo On-Chain — Template Padrão

## Quando Usar

Este skill é invocado ao **finalizar** uma análise — depois de coletar dados, rastrear hops e identificar padrões. Use para consolidar a investigação em documento estruturado.

## Template Completo

```
╔════════════════════════════════════════════════════════════╗
║         RELATÓRIO INVESTIGATIVO ON-CHAIN                   ║
╠════════════════════════════════════════════════════════════╣
║ Tipo: [ANÁLISE REAL — dados do investigador]               ║
║       [ANÁLISE SIMULADA — dados fictícios]                 ║
║ Blockchain(s): [rede(s) identificada(s)]                   ║
║ Modelo de dados: [UTXO / Account]                          ║
║ Endereço(s)/Hash: [objeto(s) da análise]                   ║
║ Data da análise: [data]                                    ║
║ Investigador: [se informado]                               ║
║ Caso/Referência: [se informado]                            ║
╚════════════════════════════════════════════════════════════╝

SEÇÃO 1 — RESUMO EXECUTIVO
─────────────────────────────────────────────────────────────
[3-5 frases descrevendo:
 • O que foi investigado
 • Principal achado
 • Conclusão principal
 • Nível de risco
 • Próximos passos recomendados]


SEÇÃO 2 — DADOS OBSERVADOS (FATOS)
─────────────────────────────────────────────────────────────
Marcar claramente: são dados extraídos do explorer pelo investigador.

• Saldo atual: [valor + moeda nativa]
• Saldo em tokens: [lista: USDT X, USDC Y, etc.]
• Volume total de entrada (IN): [valor]
• Volume total de saída (OUT): [valor]
• Período de atividade: [primeira TX → última TX]
• Total de transações: [número]
• Contrapartes principais: [endereços ou entidades identificadas]
• Interações com contratos:
  - DEX: [Uniswap, PancakeSwap, etc.]
  - Bridge: [Stargate, Wormhole, etc.]
  - Mixer: [Tornado Cash, Railgun — se houver]
  - Lending/Yield: [Aave, Compound, etc.]
  - NFT marketplaces: [OpenSea, Blur, etc.]
• Labels públicos (Etherscan/equivalente): [se houver]


SEÇÃO 3 — MAPA DE FLUXO DE FUNDOS
─────────────────────────────────────────────────────────────
[Representação textual do caminho dos fundos. Exemplo:]

[Origem (CEX/endereço externo)]
    │ [valor] [token] ─── TX: [hash] ([data/hora]) [chain]
    ▼
[Endereço investigado]
    │
    ├─ [valor] ─── TX: [hash] ──► [Destino 1]
    │                                  │
    │                                  └─ [hop seguinte]
    │
    ├─ [valor] ─── TX: [hash] ──► [Destino 2]
    │
    └─ [valor] ─── TX: [hash] ──► [Destino 3 (mixer?)]
                                      │
                                      └─ ❌ Rastreamento interrompido


SEÇÃO 4 — ANÁLISE DE PADRÕES (INFERÊNCIAS)
─────────────────────────────────────────────────────────────
Marcar claramente: são interpretações do investigador sobre os dados.

Padrões observados (ver skill /on-chain-patterns):
• [Padrão 1] — [descrição + evidência nos dados]
• [Padrão 2] — [descrição + evidência]
• [Padrão 3] — [descrição + evidência]

Hipóteses investigativas:
• [Hipótese 1] — fundamentação: [dados que suportam] / contraditório: [dados contrários]
• [Hipótese 2] — fundamentação: [...]


SEÇÃO 5 — CLASSIFICAÇÃO DE RISCO
─────────────────────────────────────────────────────────────
Nível: [BAIXO / MÉDIO / ALTO / CRÍTICO]

Justificativa:
[Base da classificação — interações suspeitas, volumes, padrões,
conexões com endereços sancionados, uso de mixers, etc.]

Indicadores de risco identificados:
☐ Interação com endereços sancionados (OFAC, blacklist Tether/Circle)
☐ Uso de mixer (Tornado Cash, Railgun)
☐ Passagem por exchange sem KYC
☐ Rapidez anormal de movimentação (horas/minutos)
☐ Fragmentação de valores (padrão de layering)
☐ Rota cross-chain para ocultação
☐ Interação com contratos conhecidamente fraudulentos
☐ Volume incompatível com atividade declarada


SEÇÃO 6 — PONTOS DE INVESTIGAÇÃO PRIORITÁRIOS
─────────────────────────────────────────────────────────────
| # | Ação Recomendada | Objetivo | Prioridade |
|---|---|---|---|
| 1 | [ação específica] | [o que resolve] | ALTA/MÉDIA/BAIXA |
| 2 | [ação] | [objetivo] | [prioridade] |
| 3 | [ação] | [objetivo] | [prioridade] |

Exemplos comuns:
• Requisição judicial à [exchange X] com o endereço de depósito [Y]
• Análise forense do contrato [Z] para identificar backdoors
• Rastreamento continuado a partir do endereço [W] na [chain]
• Cruzamento com IN 1.888/2019 via CPF do investigado
• Blacklist de stablecoin via cooperação com emissor


SEÇÃO 7 — FERRAMENTAS RECOMENDADAS
─────────────────────────────────────────────────────────────
Para aprofundar ESTA investigação:
• [Ferramenta 1] — [o que resolve + URL]
• [Ferramenta 2] — [o que resolve + URL]
• [Ferramenta 3] — [o que resolve + URL]

Ferramentas institucionais (se aplicável):
• Chainalysis Reactor — análise profissional, confirmação de clusters
• TRM Labs — triagem de risco e investigação forense
• Elliptic — compliance e conformidade regulatória


SEÇÃO 8 — LIMITAÇÕES E RESSALVAS
─────────────────────────────────────────────────────────────
• [Limitação 1: ex. dados parciais coletados]
• [Limitação 2: ex. trecho não rastreável após passagem por mixer]
• [Limitação 3: ex. ferramenta open-source usada tem precisão limitada]

⚠️ Ressalva metodológica:
Esta análise foi produzida com base nos dados fornecidos pelo
investigador e em raciocínio inferencial sobre padrões on-chain.
Os resultados devem ser validados com ferramentas profissionais
(Chainalysis, TRM, Arkham Intelligence, Elliptic) antes de uso
processual ou institucional. O Crypto Investigator não acessa
blockchains diretamente; toda análise depende de dados coletados
pelo investigador nos explorers.

═════════════════════════════════════════════════════════════
Fim do relatório.
```

## Modelo Resumido (para casos simples)

Para análises rápidas que não demandam o template completo:

```
📋 ANÁLISE RÁPIDA

Endereço: [0x...]
Blockchain: [nome]
Saldo: [valor]

🔍 OBSERVAÇÕES (fato):
• [observação 1]
• [observação 2]

🧠 INFERÊNCIAS:
• [interpretação 1] (confiança: alta/média/baixa)

🎯 AÇÃO SUGERIDA:
[próximo passo mais importante]

⚠️ Validar em ferramenta profissional antes de uso processual.
```

## Regras de Construção do Relatório

1. **FATO vs INFERÊNCIA sempre separados**
   - Seção 2 = fatos (dados extraídos)
   - Seção 4 = inferências (interpretações)

2. **Hashes e endereços completos**
   - Não abreviar em partes críticas do relatório
   - Em tabelas e mapas, usar `0xABC...123` com referência à tabela completa

3. **Timestamps padronizados**
   - UTC com offset indicado
   - Formato: DD/MM/AAAA HH:MM:SS UTC-3

4. **Valores em cripto E em BRL estimado**
   - Cripto: unidade exata (ex.: 1.23456789 BTC)
   - BRL: valor aproximado na data da TX (se possível)

5. **Linguagem adequada**
   - Estilo técnico/administrativo
   - Evitar jargão desnecessário quando o destinatário é não-técnico
   - Termos técnicos com breve explicação na primeira ocorrência

6. **Não concluir além do que os dados mostram**
   - "Os dados são compatíveis com..."
   - "É possível que..."
   - "Indica possível..."
   - NUNCA: "Está provado que..." sem evidência conclusiva

## Para Casos Simulados

Sempre incluir no cabeçalho:
```
║ Tipo: ANÁLISE SIMULADA — dados fictícios para fins didáticos
```

E no rodapé:
```
⚠️ Este é um cenário didático. Endereços, valores e datas são
fictícios. O propósito é praticar metodologia investigativa.
```

## Integração com outros skills

- Dados coletados via `/utxo-tracing`, `/account-tracing`, `/cross-chain-tracing`
- Padrões descritos em `/on-chain-patterns`
- Classificação de esquema via `/scam-patterns`
- Ações jurídicas via `/persecucao-patrimonial`
