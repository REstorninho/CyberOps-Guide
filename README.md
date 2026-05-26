# 🐱‍💻 CyberOps Terminal

> **995 commands · 33 categories · 100 online tools · standalone HTML — no install required**

A single-file offline cheatsheet for pentesters, red teamers, blue teamers, sysadmins and incident responders.  
Open `CyberOps_v17.html` directly in any browser — no server, no Node, no internet required.

---

## Screenshot

```
┌─────────────────────────────────────────────────────────────────┐
│ 🐱‍💻 CYBER_OPS  ● ONLINE  ⏱ 00:12:34  [grep commands... Ctrl+K] │
│ ALL·995  RED·468  BLUE·127  OSINT·82  OPS·274  IR·60  ▲VARS 0/26│
│ ALL OS  ⊞ WIN·272  △ NIX·623                          ★ FAVS·0  │
├───────────────────────┬─────────────────────────────────────────┤
│ ⌬ All Ops         995 │ 001  Nmap — full TCP fast scan  HIGH NIX │
│ ◈ Recon & Enum     43 │ $ nmap -p- --min-rate 5000 -T4 {RHOST}  │
│ ⊕ Bug Bounty       50 │                                   ⧉  ★  ↓│
│ ⊗ Web & API        49 │ 002  ffuf — directory brute force        │
│ ▣ Windows CMD/PS  120 │ $ ffuf -u {URL}/FUZZ -w {WORDLIST}      │
│ ...                   │                                   ⧉  ★  ↓│
└───────────────────────┴─────────────────────────────────────────┘
```

---

## Features

| Feature | Description |
|---------|-------------|
| **995 commands** | Pentest, Red Team, Blue Team, IR, Sysadmin, Cisco, OSINT |
| **33 categories** | Organised by team (RED / BLUE / IR / SYSOPS / NEUTRAL) |
| **OS Filter** | Filter by `WIN`, `NIX`, or `ALL OS` — 272 Windows, 623 Linux |
| **26 session variables** | `{LHOST}`, `{RHOST}`, `{DOMAIN}`, `{USER}`, `{HASH}`, `{TOKEN}`... substituted live in all commands |
| **Install button** | `↓` button on each card opens install instructions modal (292 tools covered) |
| **Favourites** | Star commands and filter by `★ FAVS` |
| **Copy history** | Last 25 copied commands with timestamp |
| **Search** | Full-text search across name, command, tags (`Ctrl+K`) |
| **100 online tools** | Curated links to Shodan, CyberChef, VirusTotal, SSL Labs, etc. |
| **Standalone HTML** | Single `~350 KB` file, works offline, no dependencies |
| **Android compatible** | Pure ES5 JavaScript — works on older Android WebView / Samsung Internet |

---

## Quick Start

```bash
# Just download and open:
git clone https://github.com/<your-user>/Cyberops-guide.git
cd Cyberops-guide
open CyberOps_v17.html        # macOS
xdg-open CyberOps_v17.html   # Linux
# Windows: double-click the file
```

---

## Categories

### 🔴 Red Team / Offensive (468 commands)

| Category | Count | Description |
|----------|-------|-------------|
| Recon & Enum | 43 | nmap, rustscan, ffuf, gobuster, feroxbuster |
| Bug Bounty | 50 | nuclei, httpx, katana, dalfox, pipelines |
| Web & API | 49 | sqlmap, XSStrike, wfuzz, smuggler, CORS |
| Shells & Payloads | 17 | msfvenom, pwncat, meterpreter, TTY upgrade |
| Linux PrivEsc | 21 | LinPEAS, lse, LXD/Docker abuse, SUID, LD_PRELOAD |
| Windows PrivEsc | 14 | WinPEAS, PrivescCheck, Seatbelt, UAC bypass |
| Windows CMD/PS | 120 | WMIC, LOLBins, PS pure (no modules), DPAPI, Defender |
| AD Recon | 20 | BloodHound, PowerView, netexec, ACLight |
| AD Attacks | 42 | Kerberoasting, DCSync, ADCS ESC1-8, Rubeus, Mimikatz |
| Lateral Movement | 10 | PSExec, WMI, DCOM, SMBexec |
| Persistence & C2 | 14 | Registry, WMI subscriptions, Sliver, Cobalt |
| Tunneling & Pivot | 13 | Chisel, ligolo-ng, SSH multi-hop, netsh |
| Cloud & Azure | 28 | pacu, cloudfox, ROADtools, AzureHound, prowler |
| Wireless | 12 | aircrack-ng, hcxdumptool, wifite, WEF, Proxmark3 |
| Hash Cracking | 17 | hashcat (all modes + rules), john, PMKID |
| File Transfer | 9 | certutil, BITS, SCP, python server |
| Evasion & OPSEC | 11 | AMSI bypass, donut, Nimcrypt2, timestomp |

### 🔵 Blue Team / Defensive (127 commands)

| Category | Count | Description |
|----------|-------|-------------|
| Log Analysis | 10 | Splunk, grep patterns, Windows Event IDs |
| Threat Hunting | 19 | RITA, Velociraptor, Atomic Red Team, MISP |
| Forensics & DFIR | 48 | Volatility3, chainsaw, hayabusa, KAPE, timelines |
| IR & Memory | 11 | Memory acquisition, Sysinternals, live response |
| Network Defense | 8 | Suricata, Zeek, tcpdump, tshark |
| Hardening | 8 | SSH, AppArmor, SELinux, firewall |

### 🔶 Incident Response (60 commands)

| Category | Count | Description |
|----------|-------|-------------|
| IR Windows | 21 | Triage, persistence hunt, WMI detect, KAPE, Defender |
| IR Linux | 11 | Triage script, rootkit detection, containment |
| IR M365 / Entra | 19 | UAL extraction, BEC inbox rules, MailItemsAccessed, HAWK, SPARROW |
| IR Active Directory | 9 | DCSync detect, Kerberoasting detect, ADCS, KRBTGT reset |

### ⚙️ SysOps (274 commands)

| Category | Count | Description |
|----------|-------|-------------|
| Sysadmin | 142 | Linux, Docker, Git, LVM, SSH, Proxmox, OpenWRT |
| Network Admin | 37 | tcpdump, iptables, Ubiquiti UDM, tshark |
| Cisco IOS | 95 | STP/RSTP/MSTP, HSRP/VRRP/GLBP, OSPF, EIGRP, BGP, MPLS, QoS |

### 🟢 OSINT / Misc (82 commands)

| Category | Count | Description |
|----------|-------|-------------|
| OSINT | 32 | Shodan, Maltego, TruffleHog, sherlock, OSINT Framework |
| Bug Bounty | 50 | (included in Red Team above) |
| Misc & Arsenal | 35 | ADB, apktool, JADX, Frida, autorecon, arsenal CLI |

---

## Session Variables

All `{VARIABLES}` are substituted live as you type:

```
Network:  {LHOST}  {RHOST}  {LPORT}  {RPORT}  {SUBNET}  {INTERFACE}  {PORT}
AD:       {DOMAIN}  {DC}  {DC2}  {TARGET}  {OU}  {SHARE}  {SPN}
Creds:    {USER}  {PASS}  {HASH}  {APIKEY}  {TOKEN}
Web:      {URL}
Recon:    {WORDLIST}
Files:    {FILE}  {OUTPUT}
Cloud:    {WORKSPACE}  {BUCKET}  {REGION}
```

---

## Online Tools (100 curated links)

Organised in 11 categories with search and filter:

- **Recon & OSINT** — Shodan, Censys, GreyNoise, FOFA, SecurityTrails, IntelligenceX
- **DNS** — DNSdumpster, ViewDNS, MX Toolbox, crt.sh, DNSSEC Debugger
- **SSL / TLS** — SSL Labs, badssl.com, CryptCheck, TLS Cipher Suite Search
- **Web Security** — urlscan.io, VirusTotal, Security Headers, CSP Evaluator, Observatory
- **CVE / Exploits** — Exploit-DB, sploitus, NVD, PacketStorm, 0day.today
- **Threat Intel** — abuse.ch, MalwareBazaar, MITRE ATT&CK, ThreatFox
- **Breach / Passwords** — Have I Been Pwned, DeHashed, Leak-Lookup, Grayhat S3
- **Coding & Encoding** — CyberChef, JWT.io, Regex101, explainshell, Uncoder
- **Network Tools** — ipinfo.io, Ping.eu, Online Curl, RIPE Atlas
- **Privacy** — BrowserLeaks, Panopticlick, Privacy Analyzer
- **Labs & Training** — HackTheBox, TryHackMe, PortSwigger Academy, Root-Me

---

## Data Sources

Commands and techniques aggregated from:

- [PEASS-ng](https://github.com/peass-ng/PEASS-ng) — Linux/Windows privilege escalation
- [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) — attack payloads reference
- [LOLBAS](https://lolbas-project.github.io/) — living off the land binaries (Windows)
- [GTFOBins](https://gtfobins.github.io/) — Unix binary abuse
- [WADComs](https://wadcoms.github.io/) — AD attack commands
- [infosecmatter.com](https://www.infosecmatter.com/pure-powershell-infosec-cheatsheet/) — pure PowerShell infosec
- [3os.org](https://3os.org/) — nmap, gobuster, metasploit, android, docker, linux snippets
- [Book of Secret Knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) — shell one-liners
- [rawsec.ml inventory](https://inventory.raw.pm/tools.html) — security tools catalogue
- [CISA SPARROW](https://github.com/cisagov/Sparrow) — M365 incident response
- [Mandiant Azure AD Investigator](https://github.com/mandiant/Azure_Active_Directory_Investigator)
- Custom Cisco IOS switching/routing — STP, HSRP, OSPF, BGP, MPLS, QoS
- Custom IR playbooks — Windows triage, Linux triage, M365/Entra forensics, AD recovery

---

## Tech Stack

- Pure **HTML + ES5 JavaScript** — no frameworks, no bundler, no Node required
- All data embedded as JSON — works 100% offline
- Compatible with any browser including **Android WebView** (Samsung Internet, Chrome Mobile)
- No backticks, no optional chaining, no arrow functions — maximum compatibility
- Single file `~350 KB`

---

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+K` | Focus search bar |
| `Escape` | Clear search |
| Click `⧉` | Copy command (with variable substitution) |
| Click `★` | Toggle favourite |
| Click `↓` | Show install instructions |

---

## Contributing

Pull requests welcome. To add commands, edit the `entries_v16.pkl` dataset and rebuild:

```python
import pickle

entries = pickle.load(open('entries_v16.pkl','rb'))

entries.append({
    "cat": "recon",           # category id
    "name": "Tool — description",
    "tags": ["high","lin"],   # severity + OS: win/lin + optional: ad, osep, new, blue
    "cmd":  "tool --flag {RHOST}",
    "install": "sudo apt install tool"
})

pickle.dump(entries, open('entries_v17.pkl','wb'))
```

Then replace the `var COMMANDS=` block in `CyberOps_v17.html` with the new JSON.

**Valid categories:** `recon` `web` `bugbounty` `shells` `linpriv` `winpriv` `wincmd` `adrecon` `adattack` `lateral` `persist` `tunnel` `cloud` `wireless` `crack` `transfer` `evasion` `logs` `hunt` `forensics` `dfir` `netdef` `harden` `ir_win` `ir_lin` `ir_m365` `ir_ad` `sysadmin` `netadmin` `cisco` `osint` `misc`

**Valid tags (severity):** `critical` `high` `medium` `low`  
**Valid tags (OS):** `win` `lin`  
**Valid tags (type):** `ad` `osep` `blue` `new`

---

## Disclaimer

> **For authorized use only.**  
> All techniques and commands are provided for educational purposes, legitimate security research, penetration testing on systems you own or have explicit written permission to test, and defensive/incident response operations.  
> The authors assume no responsibility for misuse.

---

## License

MIT — free to use, modify and distribute. Attribution appreciated.
