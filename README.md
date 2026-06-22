# 🐱‍💻 CYBER\_OPS Terminal

> **Referência offline para CyberOps, Pentest, Red Team, Blue Team, IR e SysOps.**  
> Ficheiro HTML único — sem dependências, sem instalação, sem internet.

---

## Visão Geral

O **CYBER\_OPS Terminal** é uma cheatsheet interactiva single-file com **1436 comandos** organizados em **41 categorias**, cobrindo toda a stack de operações de segurança — desde recon ofensivo até hardening defensivo, passando por AD attacks, Kerberos, forense, IR, cloud, container security, DevSecOps, mobile, OT/ICS, troubleshooting e reporting.

Desenhado para ser usado em campo: abre no browser, funciona offline, copia comandos com substituição automática de variáveis de sessão.

```
CYBER_OPS_TERMINAL v6.1
1436 commands · 41 categories · 102 online tools
```

---

## Início Rápido

1. Transferir `CyberOps.html`
2. Abrir no browser (Chrome, Firefox, Edge, Safari)
3. Definir variáveis de sessão (LHOST, RHOST, DOMAIN, etc.)
4. Pesquisar ou filtrar — copiar com um clique

Não requer servidor, Python, Node, nem qualquer runtime.

---

## Funcionalidades

### Filtros
| Filtro | Opções |
|---|---|
| **Team** | ALL · RED · BLUE · OSINT · OPS · IR |
| **OS** | ALL OS · WIN · NIX |
| **Domain** | ALL · RECON · WEB · CREDS · LATERAL · PRIVESC · PERSIST · EVASION · MISCONFIG · AUDIT · CVE · FORENSICS · NETWORK · CLOUD · SSL · THREAT · EXPLOIT |

### Pesquisa
- **Ctrl+K** — focar a barra de pesquisa
- Pesquisa em tempo real por nome, comando, tags e install
- **ESC** — limpar pesquisa

### Session Variables
29 variáveis substituídas automaticamente no momento de copiar, com **filtro de pesquisa** próprio no painel (por nome ou placeholder):

| Grupo | Variáveis |
|---|---|
| Network | `{LHOST}` `{RHOST}` `{HOST}` `{LPORT}` `{RPORT}` `{SUBNET}` `{INTERFACE}` `{PORT}` `{SERVER_IP}` `{CLIENT}` |
| AD | `{DOMAIN}` `{DC}` `{DC2}` `{TARGET}` `{SHARE}` `{DC_IP}` `{DC_HOSTNAME}` `{SID}` |
| Creds | `{USER}` `{PASS}` `{HASH}` `{TOKEN}` `{HASH_TYPE}` |
| Web | `{URL}` `{PHISHING_DOMAIN}` |
| Recon | `{WORDLIST}` |
| Files | `{FILE}` `{OUTPUT}` |
| Cloud | `{IMAGE}` |

### Playbooks
Sequências guiadas por cenário — em vez de procurar por categoria/tag, entra-se pelo objetivo e os comandos certos aparecem pela ordem de execução. Cada passo é um comando real (copiar / favoritar / clicar para filtrar variáveis) com uma nota de contexto. Playbooks atuais:

| Playbook | Cenário |
|---|---|
| ✉ Auditoria de domínio / email | SPF, DKIM, DMARC, DNSSEC, CAA, MTA-STS, BIMI + typosquatting/crt.sh |
| 🩸 AD takeover (red) | BloodHound → Kerberoasting/AS-REP → poisoning/relay → lateral → DCSync/Golden Ticket |
| 🚨 IR inicial Windows | Triagem de host comprometido: voláteis, persistência, rede, contas, memória, contenção |
| ◈ Recon externo de alvo | OSINT → subdomínios → portas → fingerprinting → descoberta web |

Os passos referenciam comandos por `cat::name` (zero duplicação); o `validate.py` garante que todas as referências apontam para comandos existentes.

### Outros
- **★ Favoritos** — marcar comandos para acesso rápido
- **⏱ Histórico** — últimos comandos copiados
- **⬇ Install modal** — instruções de instalação por comando
- **Online Tools** — 102 ferramentas web organizadas por categoria
- **Clock de sessão** — tempo activo desde abertura

---

## Categorias

41 categorias agrupadas por `team` (o mesmo campo usado pelo filtro Team da app):

### 🔴 RED — Offensive (20 categorias · 582 comandos)

| ID | Categoria |
|---|---|
| `recon` | Recon & Enum |
| `bugbounty` | Bug Bounty |
| `web` | Web & API |
| `shells` | Shells & Payloads |
| `linpriv` | Linux PrivEsc |
| `winpriv` | Windows PrivEsc |
| `wincmd` | Windows CMD/PS |
| `adrecon` | AD Recon |
| `adattack` | AD Attacks |
| `lateral` | Lateral Movement |
| `persist` | Persist & C2 |
| `tunnel` | Tunneling & Pivot |
| `cloud` | Cloud & Azure |
| `wireless` | Wireless |
| `crack` | Hash Cracking |
| `transfer` | File Transfer |
| `evasion` | Evasion & OPSEC |
| `phishing` | Phishing |
| `mobile` | Mobile |
| `ot_ics` | OT / ICS |

### 🔵 BLUE — Defensive (8 categorias · 307 comandos)

| ID | Categoria |
|---|---|
| `logs` | Log Analysis |
| `hunt` | Threat Hunting |
| `forensics` | Forensics & DFIR |
| `dfir` | IR & Memory |
| `netdef` | Network Defense |
| `harden` | Hardening |
| `devsecops` | DevSecOps |
| `vulnscan` | Vuln Scan |

### 🚨 IR — Incident Response (4 categorias · 70 comandos)

| ID | Categoria |
|---|---|
| `ir_win` | IR Windows |
| `ir_lin` | IR Linux |
| `ir_m365` | IR M365 / Entra |
| `ir_ad` | IR Active Directory |

### ⚙ SYSOPS (7 categorias · 386 comandos)

| ID | Categoria |
|---|---|
| `sysadmin` | Sysadmin |
| `winsrv` | Windows Server (AD/DNS/DHCP/IIS/PKI/RDS/Hyper-V) |
| `netadmin` | Network Admin |
| `troubleshoot` | Troubleshooting (inclui diagnóstico `Test-Connection`) |
| `cisco` | Cisco IOS |
| `container` | Containers (Docker/Kubernetes) |
| `reporting` | Reporting (PwnDoc/CVSS/Dradis) |

### ⌬ NEUTRAL (2 categorias · 91 comandos)

| ID | Categoria |
|---|---|
| `osint` | OSINT |
| `misc` | Misc & Arsenal |

> Online Tools (102 ferramentas web) usa um conjunto separado de categorias (`recon_osint`, `dns`, `ssl`, `web_sec`, `vuln`, `threat`, `coding`, `network`, `privacy`, `training`, `breach`) — não conta para os 41 acima.

---

## Tags

Cada comando tem tags de severidade, OS e domínio:

| Tipo | Tags |
|---|---|
| Severidade | `critical` `high` `medium` `low` |
| OS | `win` `lin` |
| Meta | `osep` `new` |
| Team flags | `blue` `red` |
| Workflow | `apply` `osint` `kerberos` `users` |
| AD | `ad` |
| Domain | `recon` `web` `creds` `lateral` `privesc` `persist` `evasion` `misconfig` `audit` `cve` `forensics` `network` `cloud` `ssl` `threat` `exploit` |
| SysOps / infra | `net` `infra` `perf` `dns` `auth` `iis` `fs` `rds` `pki` `hv` `tls` |

---

## Estrutura Técnica

```
CyberOps.html          — ficheiro único (~1.3 MB)
├── COMMANDS[]         — 1436 entradas JSON inline
├── CATEGORIES[]       — 42 definições de categoria (41 + "All Ops")
├── ONLINE_TOOLS[]     — 102 ferramentas web
├── PLAYBOOKS[]        — 4 sequências por cenário (referências cat::name)
├── TEAM_CATS{}        — mapeamento team → categorias
├── TAG_MAP{}          — 42 tags com labels e CSS
├── TOOL_TAGS{}        — ~310 ferramentas com domain tags
└── VAR_DEFS[]         — 29 variáveis de sessão (com filtro de pesquisa próprio)
```

### Estrutura de um comando
```json
{
  "cat": "adattack",
  "name": "Kerberoasting — request TGS",
  "tags": ["critical", "ad", "lin"],
  "cmd": "GetUserSPNs.py {DOMAIN}/{USER}:{PASS} -dc-ip {DC} -request -outputfile kerb.hash",
  "install": "https://github.com/fortra/impacket"
}
```

### Campo `install`

| Valor | Significado |
|---|---|
| `native://windows` | Nativo do Windows — não precisa instalar |
| `native://linux` | Nativo do Linux |
| `native://cisco` | Nativo do IOS |
| `native://manual` | Uso manual (browser, GUI, etc.) |
| `https://...` | URL de download/repositório |
| `pip3 install ...` | Comando de instalação directo |

---

## Convenções

- **`{RHOST}`** — IP/hostname do alvo em contextos de rede e scanning
- **`{HOST}`** — Hostname/IP usado em diagnóstico/troubleshooting (ex.: `Test-Connection`)
- **`{TARGET}`** — Nome de objecto AD (utilizador, computador, grupo)
- Comandos ordenados por severidade: `critical → high → medium → low`
- Comandos multi-linha usam `\n` no campo `cmd`

---

## Aviso Legal

```
⚠ Usar apenas em sistemas com autorização escrita.
Pentest e red team sem autorização é ilegal.
```

---

## Desenvolvimento

O projecto foi desenvolvido de forma iterativa com as seguintes milestones:

- **v1–v5** — Base inicial: recon, web, AD, shells, lateral, persist, evasion
- **v6** — Expansão major: Windows Server, Kerberos, container, phishing, DevSecOps, mobile, OT/ICS, reporting, vuln scanning, Sysinternals, IR
- **v6.1** — Estabilização: standardização de variáveis, install fields completos, ordenação por severidade, sistema de domain tags, bug fixes de runtime (mobile browser, anti-recursion, rendering resilience)
- **v6.1.x** — Troubleshooting de rede: 8 cheat sheets de `Test-Connection` (ping, TCP port, jitter/packet loss, traceroute/MTU, sweep de hosts, fonte/IPv4-IPv6, monitorização contínua, erros comuns); variável `{HOST}`; alternativas `Test-NetConnection`/`TcpClient` para compatibilidade com Windows PowerShell 5.1 (`-TcpPort` só existe em PS7+); filtro de pesquisa no painel `SESSION_VARIABLES`; clique num comando filtra automaticamente o painel `SESSION_VARIABLES` para mostrar apenas as variáveis usadas nesse comando
- **v6.2** — Auditoria de segurança de domínios/email: 13 cheat sheets de SPF, DKIM (verificação e brute-force de selectors), DMARC (registo e auditoria de política), DNSSEC, CAA, MTA-STS, TLS-RPT, BIMI e um script de auditoria completa (bash + PowerShell); 2 ferramentas online adicionadas (dmarcian DMARC Inspector, Mail-Tester)
- **v6.3** — OSINT avançado: 15 cheat sheets — typosquatting + Certificate Transparency (`dnstwist`/`crt.sh`), trace de phishing M365 (`Get-MessageTrace`, categoria `ir_m365`), threat intel de IPs (GreyNoise, Censys, Onyphe), leak/breach search (LeakIX, DeHashed), recon de empresa (Hunter.io), OSINT de contas Google (`GHunt`), endpoints arquivados em massa (`waybackurls`+`gau`), metadata de documentos (`Metagoofil`), crawler OSINT (`Photon`), fingerprinting `.onion` (`OnionScan`), histórico de WHOIS (Whoxy)
- **v6.4** — Qualidade & CI: `validate.py` (gate de integridade — parsing dos arrays, `node --check`, unicidade de `(cat, name)`, validação de categorias/tags/install) ligado a um GitHub Action (`.github/workflows/validate.yml`) que corre em cada push/PR; 11 tags órfãs (`net`, `infra`, `perf`, `dns`, `auth`, `iis`, `fs`, `rds`, `pki`, `hv`, `tls`) adicionadas ao `TAG_MAP` com badges/CSS próprios (antes renderizavam invisíveis); severidade em falta corrigida em 11 comandos
- **v6.5** — Descoberta por cenário: novo separador **PLAYBOOKS** com 4 sequências curadas (Auditoria de domínio/email, AD takeover, IR inicial Windows, Recon externo de alvo). Camada de índice por cima dos comandos (array `PLAYBOOKS` só com referências `cat::name`, zero duplicação); reutiliza os cards existentes (copy/fav/filtro de variáveis); `validate.py` valida que cada passo aponta para um comando real

### Bugs Resolvidos (v6.1)
- `</script>` dentro de strings JS fechava o bloco prematuramente
- CRLF nas linhas causava inversão de ordem no clipboard PowerShell
- `var VAR_DEFS=` removido por str_replace — causava SyntaxError
- TEAM_CATS incompleto — 261 comandos invisíveis nos filtros de team
- `activeCat=''` em mobile browsers — todos os filtros mostravam 0 resultados
- `buildNav()` sem guard anti-recursão — risco de loop infinito em mobile
- `_renderGrid()` sem try/catch — um comando corrompido interrompia o rendering
- 32 comandos Windows com tag `lin` em vez de `win`
- 6 chaves duplicadas em TOOL_TAGS
- Tags orphaned (`blue`, `red`, `apply`, `osint`, `kerberos`, `users`) sem badge visual
