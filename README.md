# 🐱‍💻 CYBER\_OPS Terminal

> **Referência offline para CyberOps, Pentest, Red Team, Blue Team, IR e SysOps.**  
> Ficheiro HTML único — sem dependências, sem instalação, sem internet.

---

## Visão Geral

O **CYBER\_OPS Terminal** é uma cheatsheet interactiva single-file com **1384 comandos** organizados em **42 categorias**, cobrindo toda a stack de operações de segurança — desde recon ofensivo até hardening defensivo, passando por AD attacks, Kerberos, forense, IR, cloud, container security, DevSecOps, mobile, OT/ICS e reporting.

Desenhado para ser usado em campo: abre no browser, funciona offline, copia comandos com substituição automática de variáveis de sessão.

```
CYBER_OPS_TERMINAL v6.1
1384 commands · 42 categories · 100 online tools
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
26 variáveis substituídas automaticamente no momento de copiar:

| Grupo | Variáveis |
|---|---|
| Network | `{LHOST}` `{RHOST}` `{LPORT}` `{RPORT}` `{SUBNET}` `{INTERFACE}` `{PORT}` |
| AD | `{DOMAIN}` `{DC}` `{DC2}` `{SPN}` `{TARGET}` `{OU}` `{SHARE}` |
| Creds | `{USER}` `{PASS}` `{HASH}` `{APIKEY}` `{TOKEN}` |
| Web | `{URL}` |
| Recon | `{WORDLIST}` |
| Files | `{FILE}` `{OUTPUT}` |
| Cloud | `{WORKSPACE}` `{BUCKET}` `{REGION}` |

### Outros
- **★ Favoritos** — marcar comandos para acesso rápido
- **⏱ Histórico** — últimos comandos copiados
- **⬇ Install modal** — instruções de instalação por comando
- **Online Tools** — 100 ferramentas web organizadas por categoria
- **Clock de sessão** — tempo activo desde abertura

---

## Categorias

### 🔴 RED — Offensive (19 categorias · 561 comandos)

| ID | Categoria |
|---|---|
| `recon` | Recon & Scanning |
| `web` | Web Exploitation |
| `shells` | Shells & Listeners |
| `linpriv` | Linux Privilege Escalation |
| `winpriv` | Windows Privilege Escalation |
| `wincmd` | Windows Post-Exploitation |
| `adrecon` | AD Enumeration |
| `adattack` | AD Attacks |
| `lateral` | Lateral Movement |
| `persist` | Persistence & C2 |
| `tunnel` | Tunnelling & Pivoting |
| `cloud` | Cloud (AWS/Azure/GCP) |
| `wireless` | Wireless & RF |
| `crack` | Password Cracking |
| `transfer` | File Transfer |
| `evasion` | AV/EDR Evasion |
| `mobile` | Mobile (Android/iOS) |
| `ot_ics` | OT/ICS |
| `phishing` | Phishing & Social Engineering |

### 🔵 BLUE — Defensive (8 categorias · 298 comandos)

| ID | Categoria |
|---|---|
| `logs` | Log Analysis |
| `hunt` | Threat Hunting |
| `forensics` | Digital Forensics |
| `dfir` | DFIR & Sysinternals |
| `netdef` | Network Defence |
| `harden` | Hardening & Audit |
| `devsecops` | DevSecOps |
| `vulnscan` | Vulnerability Scanning |

### 🌐 OSINT (13 categorias · 77 comandos)

`osint` · `bugbounty` · `recon_osint` · `breach` · `threat` · `dns` · `ssl` · `web_sec` · `vuln` · `coding` · `network` · `privacy` · `training`

### ⚙ SYSOPS (8 categorias · 377 comandos)

| ID | Categoria |
|---|---|
| `sysadmin` | Linux SysAdmin |
| `netadmin` | Network Admin |
| `cisco` | Cisco IOS |
| `winsrv` | Windows Server (AD/DNS/DHCP/IIS/PKI/RDS/Hyper-V) |
| `container` | Container Security (Docker/Kubernetes) |
| `troubleshoot` | Troubleshooting |
| `reporting` | Reporting (PwnDoc/CVSS/Dradis) |
| `misc` | Misc Tools |

### 🚨 IR — Incident Response (4 categorias · 69 comandos)

`ir_win` · `ir_lin` · `ir_m365` · `ir_ad`

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

---

## Estrutura Técnica

```
CyberOps.html          — ficheiro único (~1.2 MB)
├── COMMANDS[]         — 1384 entradas JSON inline
├── CATEGORIES[]       — 42 definições de categoria
├── ONLINE_TOOLS[]     — 100 ferramentas web
├── TEAM_CATS{}        — mapeamento team → categorias
├── TAG_MAP{}          — 31 tags com labels e CSS
├── TOOL_TAGS{}        — ~310 ferramentas com domain tags
└── VAR_DEFS[]         — 26 variáveis de sessão
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
