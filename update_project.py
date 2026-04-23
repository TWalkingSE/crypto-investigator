import os
import glob

base_dir = os.path.dirname(os.path.abspath(__file__))

# 1. Enhance existing wrappers
def enhance_wrappers(directory):
    path = os.path.join(base_dir, directory, "*.md")
    for filepath in glob.glob(path):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if "INSTRUÇÃO DE SISTEMA: Você DEVE ler e carregar imediatamente o arquivo:" not in content:
            # Replace the old soft instruction with a hard instruction
            content = content.replace("Leia o arquivo canônico para as instruções completas.", 
                                      "INSTRUÇÃO DE SISTEMA: Você DEVE usar sua ferramenta de leitura de arquivos para ler e seguir imediatamente o arquivo canônico acima. Não prossiga sem ler o arquivo canônico.")
            # Also if it's the old format without the replace string:
            if "INSTRUÇÃO DE SISTEMA" not in content:
                content += "\n\nINSTRUÇÃO DE SISTEMA: Você DEVE usar sua ferramenta de leitura de arquivos para ler e seguir imediatamente o arquivo canônico acima."
                
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

enhance_wrappers(r".claude\skills")
enhance_wrappers(r".windsurf\skills")

# 2. Create new skills in .github/skills/
new_skills = {
    "investigator-opsec": {
        "desc": "OpSec (Segurança Operacional) para o investigador: isolamento de ambiente, interação segura com dApps, proteção de IP e uso de VPN/Tor.",
        "content": """# investigator-opsec

## Objetivo
Garantir a Segurança Operacional (OpSec) do investigador durante a análise de criptoativos, evitando exposição de IP, infecção por malware, vazamento de informações do caso ou comprometimento de carteiras institucionais.

## Regras de OpSec
1. **Nunca use carteiras pessoais** para interagir com contratos suspeitos ou receber fundos de casos.
2. **Isolamento de Rede:** Use VPNs no-log ou a rede Tor ao consultar explorers, APIs ou interagir com dApps. Muitos dApps falsos coletam IPs.
3. **VM ou Sandbox:** Ao baixar executáveis, scripts Python ou planilhas de casos de vítimas, isole-os em Máquinas Virtuais.
4. **RPCs Seguros:** Ao configurar MetaMask/Rabby para análise, use RPCs públicos que não rastreiam IP (ex: Ankr, 1RPC) ou rode um node local.
5. **Cuidado com Dust Attacks:** Se a carteira institucional receber tokens desconhecidos (dust), nunca interaja ou tente vendê-los. É uma tática de desanonimização ou phishing de aprovação.

## Procedimento
- Avalie o risco da ferramenta antes de acessá-la.
- Instrua o investigador a não clicar em links fornecidos por supostos "suportes" ou hackers.
- Se houver necessidade de interagir on-chain (ex: aprovar transação para resgate), use uma carteira burn (descartável).
"""
    },
    "case-management": {
        "desc": "Gerenciamento do caso e da investigação: criação e manutenção de CASE_LOG.md e documentação contínua.",
        "content": """# case-management

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
"""
    },
    "hardware-wallet-forensics": {
        "desc": "Procedimentos forenses para apreensão, isolamento e extração segura de hardware wallets (Ledger, Trezor) e seed phrases.",
        "content": """# hardware-wallet-forensics

## Objetivo
Orientar a apreensão física, isolamento de radiofrequência e extração forense de criptoativos armazenados em hardware wallets (Trezor, Ledger, Keystone) e a custódia de seed phrases.

## Procedimento de Busca e Apreensão Física
1. **Isolamento Imediato:** Utilize Faraday bags para isolar smartphones, laptops ou hardware wallets Bluetooth (ex: Ledger Nano X) para evitar "remote wipe" (limpeza remota).
2. **Busca de Sementes (Seed Phrases):** A prioridade em campo não é apenas o dispositivo, mas o papel, placa de metal (Cryptosteel) ou gerenciador de senhas contendo as 12/24 palavras.
3. **Fotografia e Cadeia de Custódia:** Fotografe a tela de dispositivos logados ANTES de qualquer interação.
4. **Extração de Fundos (Transferência Legal):**
   - A transferência de ativos apreendidos deve ir para uma carteira sob controle do Estado (Judiciário/Polícia).
   - Requer autorização judicial explícita.
   - **Atenção à Taxa de Rede (Gas):** A carteira apreendida precisa ter saldo nativo (ETH, BTC, TRX) para pagar a taxa de transferência. Nunca envie fundos da carteira da instituição para a do investigado; use uma "funding wallet" isolada se necessário.
5. **Aviso:** Nunca digite uma seed phrase apreendida em um dispositivo conectado à internet (computador de trabalho). Use um dispositivo air-gapped ou uma hardware wallet limpa para restauração.
"""
    }
}

for skill_name, data in new_skills.items():
    # 1. Create .github/skills/ dir and SKILL.md
    skill_dir = os.path.join(base_dir, ".github", "skills", skill_name)
    os.makedirs(skill_dir, exist_ok=True)
    
    skill_content = f\"\"\"---
name: {skill_name}
description: {data['desc']}
---

{data['content']}\"\"\"
    with open(os.path.join(skill_dir, "SKILL.md"), "w", encoding="utf-8") as f:
        f.write(skill_content)
    
    # 2. Create .claude/skills/ wrapper
    claude_wrapper_content = f"""---
name: {skill_name}
description: {data['desc']}
---

# {skill_name}

Este skill é um wrapper de descoberta. O conteúdo canônico está em:

`.github/skills/{skill_name}/SKILL.md`

INSTRUÇÃO DE SISTEMA: Você DEVE usar sua ferramenta de leitura de arquivos para ler e seguir imediatamente o arquivo canônico acima. Não prossiga sem ler o arquivo canônico.
"""
    with open(os.path.join(base_dir, ".claude", "skills", f"{skill_name}.md"), "w", encoding="utf-8") as f:
        f.write(claude_wrapper_content)
        
    # 3. Create .windsurf/skills/ wrapper (same content)
    with open(os.path.join(base_dir, ".windsurf", "skills", f"{skill_name}.md"), "w", encoding="utf-8") as f:
        f.write(claude_wrapper_content)

# 3. Create local-ai-privacy.md in references
ref_path = os.path.join(base_dir, ".github", "skills", "crypto-tools-kb", "references", "local-ai-privacy.md")
local_ai_content = """# IA Local e Privacidade na Investigação (Local AI)

O uso de IA baseada em nuvem (OpenAI, Anthropic) para analisar dumps de transações, listas de endereços ou históricos de chat pode violar políticas de sigilo da investigação e expor PII (Personally Identifiable Information).

## Soluções Locais (Offline)
- **Ollama:** Permite rodar modelos LLM (Llama 3, Mistral) inteiramente offline no computador do investigador. Ideal para processar grandes listas de endereços e extrair padrões.
- **LM Studio / GPT4All:** Interfaces gráficas fáceis de instalar para rodar modelos locais sem configuração complexa.
- **Any-Sync / Local RAG:** Ferramentas de RAG (Retrieval-Augmented Generation) locais para fazer perguntas aos autos do processo sem vazar dados para a internet.

## Boas Práticas
1. Anonimize ou pseudonimize os endereços `0x...` e transações antes de jogar em LLMs de nuvem, se o uso local não for possível.
2. Não faça upload de sentenças não públicas, quebras de sigilo bancário ou relatórios confidenciais (ex: RIF do COAF) para serviços web de IA.
"""
with open(ref_path, "w", encoding="utf-8") as f:
    f.write(local_ai_content)

# 4. Update README.md
readme_path = os.path.join(base_dir, "README.md")
with open(readme_path, "r", encoding="utf-8") as f:
    readme = f.read()

# Update badge to 15 skills
readme = readme.replace("![Agent Skills](https://img.shields.io/badge/Agent%20Skills-12-7c3aed)", "![Agent Skills](https://img.shields.io/badge/Agent%20Skills-15-7c3aed)")
readme = readme.replace("12 agent skills", "15 agent skills")
readme = readme.replace("12 skills canônicos", "15 skills canônicos")
readme = readme.replace("12 wrappers", "15 wrappers")

# Add to skills table
skills_table_addition = """| `/investigator-opsec` | Segurança Operacional (OpSec) para o investigador |
| `/case-management` | Gerenciamento e documentação contínua do caso |
| `/hardware-wallet-forensics` | Procedimentos para apreensão física de hardware wallets |
"""
readme = readme.replace("| `/crypto-tools-kb` | Base de conhecimento com 100+ ferramentas |", 
                        "| `/crypto-tools-kb` | Base de conhecimento com 100+ ferramentas |\n" + skills_table_addition)

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme)

# 5. Update AGENTS.md
agents_path = os.path.join(base_dir, "AGENTS.md")
with open(agents_path, "r", encoding="utf-8") as f:
    agents = f.read()

agents_skills_addition = """- `/investigator-opsec` — Segurança Operacional (OpSec) para o investigador
- `/case-management` — Gerenciamento e documentação contínua do caso (CASE_LOG)
- `/hardware-wallet-forensics` — Apreensão física e extração de hardware wallets e seed phrases
"""
agents = agents.replace("- `/crypto-tools-kb` — Base de conhecimento de ferramentas OSINT e forenses",
                        "- `/crypto-tools-kb` — Base de conhecimento de ferramentas OSINT e forenses\n" + agents_skills_addition)

with open(agents_path, "w", encoding="utf-8") as f:
    f.write(agents)

# 6. Update CLAUDE.md
claude_path = os.path.join(base_dir, "CLAUDE.md")
with open(claude_path, "r", encoding="utf-8") as f:
    claude = f.read()

claude_addition = """[10] Investigator OpSec (Proteção do Investigador)
[11] Hardware Wallet Forensics (Apreensão Física)
"""
claude = claude.replace("[9] Roteiro de estudo personalizado\n",
                        "[9] Roteiro de estudo personalizado\n" + claude_addition)

with open(claude_path, "w", encoding="utf-8") as f:
    f.write(claude)

print("Update completed successfully.")
