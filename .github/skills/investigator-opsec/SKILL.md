---
name: investigator-opsec
description: OpSec (Segurança Operacional) para o investigador: isolamento de ambiente, interação segura com dApps, proteção de IP e uso de VPN/Tor.
---

# investigator-opsec

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
