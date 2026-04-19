# Ferramentas CLI e Open-Source

Para investigadores que preferem linha de comando, automação e ferramentas auditáveis.

## Frameworks de Análise

| Ferramenta | Linguagem | URL |
|---|---|---|
| BlockSci | C++/Python | github.com/citp/BlockSci |
| GraphSense | Python/Scala | graphsense.info |
| Ethereum ETL | Python | github.com/blockchain-etl/ethereum-etl |
| Bitcoin ETL | Python | github.com/blockchain-etl/bitcoin-etl |
| Multichain ETL | Python | github.com/blockchain-etl |

## Bitcoin CLI

| Ferramenta | URL |
|---|---|
| Bitcoin Core (bitcoind + bitcoin-cli) | bitcoincore.org |
| Electrum Personal Server | github.com/chris-belcher/electrum-personal-server |
| Fulcrum | github.com/cculianu/Fulcrum |
| Esplora | github.com/Blockstream/esplora (self-hostable Blockstream explorer) |

## Ethereum / EVM CLI

| Ferramenta | Função | URL |
|---|---|---|
| Foundry (cast) | CLI completo para EVM | getfoundry.sh |
| ethers.js / web3.js | Libs JavaScript | ethers.org, web3js.readthedocs.io |
| Hardhat | Framework de dev + análise | hardhat.org |
| Tenderly CLI | Debugging | tenderly.co |
| Brownie | Python framework | eth-brownie.readthedocs.io |
| Web3.py | Python | web3py.readthedocs.io |

## Análise de Smart Contracts

| Ferramenta | Função | URL |
|---|---|---|
| Slither | Análise estática Solidity | github.com/crytic/slither |
| Mythril | Execução simbólica EVM | github.com/ConsenSys/mythril |
| Echidna | Fuzzing | github.com/crytic/echidna |
| Manticore | Execução simbólica | github.com/trailofbits/manticore |
| Surya | Inspeção de código | github.com/ConsenSys/surya |
| Aderyn | Static analyzer (Rust) | github.com/Cyfrin/aderyn |
| 4naly3er | Automated analyzer | github.com/Picodes/4naly3er |

## Indexação de Dados On-Chain

| Ferramenta | Uso | URL |
|---|---|---|
| The Graph | Indexação GraphQL de contratos | thegraph.com |
| Subsquid | Indexer multi-chain | subsquid.io |
| Goldsky | Real-time subgraphs | goldsky.com |
| Ponder | Indexer tipado | ponder.sh |
| Envio | HyperIndex (Rust) | envio.dev |

## Bancos de Dados On-Chain

| Dataset | Acesso | URL |
|---|---|---|
| Google BigQuery Public Datasets | SQL em dados BTC/ETH/etc. | cloud.google.com/bigquery/public-data |
| Dune Analytics | SQL querying com dashboards | dune.com |
| Flipside Crypto | SQL via interface | flipsidecrypto.xyz |
| Allium | Dados enterprise | allium.so |
| Transpose | Real-time SQL | transpose.io |

## Wallet / Endereço Queries

| Ferramenta | URL |
|---|---|
| Alchemy API | alchemy.com |
| Infura API | infura.io |
| QuickNode | quicknode.com |
| Moralis API | moralis.io |
| Chainbase | chainbase.com |
| Covalent | covalenthq.com |
| Mobula | mobula.io |

## Segurança e Forense (OSINT geral)

| Ferramenta | Função | URL |
|---|---|---|
| SpiderFoot | OSINT automatizado | spiderfoot.net |
| Maltego | Link analysis com transforms cripto | maltego.com |
| TheHarvester | OSINT de e-mails/domínios | github.com/laramies/theHarvester |
| Recon-ng | Framework OSINT | github.com/lanmaster53/recon-ng |

## Parsing e Análise de Dados

| Ferramenta | Uso |
|---|---|
| Python + pandas | Análise de CSV de TX |
| SQL (SQLite, Postgres) | Queries locais |
| jq | Manipulação de JSON |
| Rust tools (etheroll-rs, etc.) | Performance |

## Exemplos de Uso (Bitcoin via bitcoin-cli)

```bash
# Informações sobre endereço (necessita wallet indexada)
bitcoin-cli getaddressinfo "bc1q..."

# Histórico de transações (via esplora API)
curl https://blockstream.info/api/address/bc1q.../txs

# Total recebido/enviado
curl https://blockstream.info/api/address/bc1q...
```

## Exemplos de Uso (Ethereum via cast)

```bash
# Saldo
cast balance 0xABC... --rpc-url $RPC

# Código do contrato
cast code 0xABC... --rpc-url $RPC

# Chamar função read
cast call 0xABC... "balanceOf(address)(uint256)" 0xXYZ... --rpc-url $RPC

# Decodificar TX
cast run 0xHASH... --rpc-url $RPC
```

## Por Que Usar CLI/Open-Source

- **Auditável**: código-fonte público, sem black-box
- **Reproduzível**: análises podem ser replicadas por terceiros
- **Offline**: pode rodar em air-gapped
- **Customizável**: adapte para necessidades específicas
- **Sem limite de API**: com node próprio, sem rate limits
- **Aceitação forense**: ferramentas auditáveis são preferidas em contexto judicial
