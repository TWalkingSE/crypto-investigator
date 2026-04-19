# Contribuindo com o Crypto Investigator

Contribuições são muito bem-vindas! Este projeto é mantido por investigadores e profissionais que lidam com criptoativos — seu conhecimento prático é valioso.

## Formas de Contribuir

1. **Corrigir erros** em skills existentes (informações desatualizadas, links quebrados)
2. **Adicionar ferramentas** à base de conhecimento (skill `crypto-tools-kb`)
3. **Novos cenários** de simulação em `simulacao-investigacao`
4. **Melhorar padrões** em `on-chain-patterns` com casos documentados
5. **Atualizar legislação** em `persecucao-patrimonial` e referência Brasil
6. **Traduzir** skills ou referências
7. **Reportar bugs** ou comportamentos inesperados
8. **Propor novos skills** para áreas não cobertas

## Como Contribuir

### Pequenas Correções

Para correções simples (typo, link, atualização pontual):

1. Fork o repositório
2. Edite o arquivo diretamente no GitHub (botão de lápis)
3. Abra um Pull Request descrevendo a mudança

### Contribuições Maiores

Para mudanças significativas:

1. Abra uma **Issue** antes descrevendo a proposta
2. Aguarde feedback (mantenedores comentarão)
3. Fork o repositório, crie uma branch: `git checkout -b feature/nome-descritivo`
4. Faça as mudanças seguindo o padrão existente
5. Atualize o CHANGELOG.md na seção `[Unreleased]`
6. Abra um Pull Request referenciando a Issue

## Padrões de Qualidade

### Skills Novos

Cada skill deve ter:

```yaml
---
name: nome-do-skill
description: >
  Descrição clara em 1-3 frases. Use essa descrição para indicar QUANDO o 
  skill deve ser usado, com palavras-chave que o agente possa reconhecer 
  ao processar a pergunta do usuário.
---
```

Conteúdo:
- Introdução clara (o que e quando usar)
- Protocolo ou procedimento passo a passo
- Tabelas de ferramentas/referências quando aplicável
- Exemplos concretos
- Integração com outros skills relacionados (links internos)
- Entre 50 e 500 linhas — se ultrapassar, considere dividir em skill principal + arquivos em `references/`

### Ferramentas Adicionadas à KB

Ao sugerir uma ferramenta para `crypto-tools-kb`:

- **Nome oficial** e **URL** (sem redirects)
- **Categoria** (explorer, analytics, forense, etc.)
- **Chains cobertas**
- **Custo** (gratuito / freemium / pago / licença institucional)
- **Diferencial** (o que a torna relevante vs. alternativas)
- **Alertas de incidentes** (se houver)
- **Idioma** principal da interface

### Cenários de Simulação

Ao adicionar cenários em `simulacao-investigacao`:

- **Dados 100% fictícios** — nunca reproduzir caso real em andamento
- Endereços e hashes inventados mas com formato válido
- Timestamps coerentes
- Contexto plausível (inspirado em tipologias reais sem identificar vítimas/acusados reais)
- Incluir **gabarito completo** após o enunciado

## O Que NÃO Aceitar

- Informações sobre casos reais em investigação em andamento
- Endereços ou hashes de vítimas/acusados identificáveis
- Recomendações de ferramentas comprovadamente fraudulentas
- Ferramentas com histórico grave sem sinalização (ex: não recomendar Avast sem alertar do incidente Jumpshot)
- Orientação que possa ser usada para facilitar crime
- Conteúdo que viole LGPD, Marco Civil ou direito processual brasileiro
- Jurisprudência inventada — cite apenas o que existe
- **Painéis clandestinos** ou ferramentas que alimentam-se de dados obtidos ilegalmente

## Código de Conduta

Ao contribuir, você concorda com o [Código de Conduta](CODE_OF_CONDUCT.md) do projeto, baseado no Contributor Covenant 2.1.

## Revisão

Pull requests são revisados por mantenedores. O processo típico:

1. **Revisão técnica**: o conteúdo está correto? É útil?
2. **Revisão de estilo**: segue o padrão do projeto?
3. **Revisão de segurança**: não introduz risco ou conteúdo inadequado?
4. **Feedback**: pode haver pedidos de ajuste
5. **Merge**: aprovação → merge na main

## Licença das Contribuições

Ao submeter um Pull Request, você concorda em licenciar sua contribuição sob a mesma licença do projeto ([MIT](LICENSE)).

## Dúvidas?

- Abra uma **Issue** marcada como `question`
- Ou entre em contato com os mantenedores conforme instruído no repositório

Obrigado por contribuir!
