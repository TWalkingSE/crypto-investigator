---
name: case-management
description: Gerenciamento do caso e da investigação: criação e manutenção de CASE_LOG.md e documentação contínua.
---

# case-management

## Objetivo
Manter o histórico da investigação organizado, documentando evidências, hipóteses e resultados em um `CASE_LOG.md` persistente.

## Procedimento de Gestão
1. **Inicialização:** Ao iniciar um novo caso, crie um arquivo `CASE_LOG.md` no diretório local.
2. **Estrutura do CASE_LOG.md:**
   - **ID do Caso / Data**
   - **Escopo Inicial:** O que estamos buscando? (Ex: Rastrear saída de fundos do endereço X).
   - **Endereços de Interesse (IoCs):** Lista de carteiras, hashes e anotações parciais.
   - **Hipóteses Atuais:** O que acreditamos ter acontecido.
   - **Tarefas Pendentes:** Próximos saltos a analisar, blockchains a verificar.
3. **Atualização Contínua:** Após cada análise de transação significativa, atualize o `CASE_LOG.md`.
4. **Encerramento:** Quando a investigação parar por limite técnico ou conclusão, consolide o `CASE_LOG.md` e gere o relatório final com `/investigation-report`.
