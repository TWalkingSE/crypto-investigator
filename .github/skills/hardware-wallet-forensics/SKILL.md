---
name: hardware-wallet-forensics
description: Procedimentos forenses para apreensão, isolamento e extração segura de hardware wallets (Ledger, Trezor) e seed phrases.
---

# hardware-wallet-forensics

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
