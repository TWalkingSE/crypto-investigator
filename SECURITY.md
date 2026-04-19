# Política de Segurança

## Natureza do Projeto

O Crypto Investigator é um projeto de **instruções e conhecimento** — não é software executável com vetores tradicionais de vulnerabilidade. Ele consiste em arquivos Markdown lidos por agentes de IA em IDEs.

Apesar disso, há categorias de problemas que devem ser reportados.

## O Que Reportar

### Problemas de Segurança Aplicáveis

- **Instruções que possam facilitar crime** se aplicadas inadequadamente
- **Orientação que viole LGPD, Marco Civil ou direito processual brasileiro**
- **Ferramentas comprometidas** incluídas na KB sem alerta
- **Endereços ou dados reais** que acidentalmente tenham vazado para os arquivos do projeto
- **Jurisprudência fabricada** ou legislação citada incorretamente
- **Vulnerabilidades em qualquer script** que venha a ser adicionado ao repositório
- **Técnicas que contornem proteções éticas** em IDEs agentic

### Não-Problemas de Segurança

- Discordâncias metodológicas → abrir Issue normal
- Ferramentas faltando → Pull Request com adição
- Typos → Pull Request com correção
- Sugestões de melhoria → Issue de enhancement

## Como Reportar

### Reportes Não-Sensíveis

Abra uma **Issue** marcada como `security` ou `compliance` e descreva o problema abertamente.

### Reportes Sensíveis

Para problemas que **não devem** ser discutidos publicamente (ex: vulnerabilidade ativa, dados reais que vazaram):

1. **NÃO** abra Issue pública
2. Contate os mantenedores via:
   - E-mail privado do mantenedor (ver perfil do GitHub)
   - Mensagem direta via GitHub

Aguardaremos até **7 dias** para responder. Em seguida:
- Validação do problema
- Plano de correção
- Disclosure coordenado (se aplicável)
- Agradecimento no CHANGELOG (se desejar)

## Práticas de Segurança do Usuário

Ao usar o Crypto Investigator em investigações reais:

### Dados de Investigação

- **NUNCA** commite arquivos de caso real no repositório
- Mantenha `cases/`, `investigations/`, `evidence/` fora do controle de versão (já incluído em `.gitignore`)
- Use pastas isoladas em ambiente próprio
- Considere usar Git privado ou ferramentas dedicadas para case management

### Chaves Privadas e Seeds

- **JAMAIS** compartilhe chaves privadas ou seed phrases com o agente de IA
- Se receber seed apreendida, manuseie conforme protocolo pericial
- Não digite seeds em dispositivos conectados à internet quando possível
- Use cold wallet institucional para apreensões

### Exposição de Dados ao Agente

- O Crypto Investigator é **um guia** — dados fornecidos no chat vão para o modelo de IA do provedor (Anthropic, OpenAI, Google)
- Para casos **altamente sensíveis**, considere:
  - LLMs locais (Ollama, LM Studio) com este projeto
  - Modelos com políticas de zero-retention (OpenAI API com opt-out, Claude via API)
  - Anonimização de endereços antes de discutir com o agente

### Cadeia de Custódia Digital

- Documente cada passo da análise
- Capturas de tela com timestamps
- Hashes dos arquivos de evidência
- Não modifique dados originais — trabalhe em cópias

## Isenção de Responsabilidade

Este projeto é fornecido "como está", sem garantias. Orientações aqui são **educacionais** e devem ser validadas em contexto de caso real por profissionais qualificados (perito em criptoativos, advogado, especialista técnico).

Os mantenedores não se responsabilizam por uso inadequado ou aplicação fora de contexto das orientações contidas neste projeto.
