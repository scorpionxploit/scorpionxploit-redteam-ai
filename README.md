# scorpionxploit-redteam-ai

> **Deconstructing threats. Demystifying defense.**  
> Autonomous AI adversary emulation & purple team attack path graph explorer.

[![CI](https://github.com/scorpionxploit/scorpionxploit-redteam-ai/actions/workflows/ci.yml/badge.svg)](https://github.com/scorpionxploit/scorpionxploit-redteam-ai/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-10B981.svg)](LICENSE)
[![Security Audit: Passed](https://img.shields.io/badge/Security%20Audit-Passed-38BDF8.svg)](AUDIT.md)
[![MITRE ATT&CK](https://img.shields.io/badge/MITRE-ATT%26CK%20v14-orange.svg)](https://attack.mitre.org)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)

## Overview
**scorpionxploit-redteam-ai** is an open-source offensive security and purple-teaming framework engineered by **Aditya Sharma (ScorpionXploit)**. It bridges the gap between offensive adversary simulation and defensive telemetry validation by autonomously executing benign, MITRE ATT&CK-mapped adversary behaviors to evaluate whether your EDR, SIEM, and SOC analysts can detect real-world tactics.

### Strict Ethical Guardrails
- **Cryptographic Authorization Gate**: Every simulation run requires an HMAC-SHA256 signed run token tied to the authorized hostname and timestamp window.
- **Benign-by-Design Emulation**: Actions use safe canary markers (`X-Canary-Probe`) and read-only non-destructive system calls.
- **Zero Exploit Weaponization**: The agent tests telemetry visibility and behavioral signatures, never deploying destructive payloads.

## Key Features
1. **MITRE ATT&CK Kill-Chain Modeler**: Maps attack vectors across Discovery, Execution, Persistence, and Command & Control.
2. **Detection Efficacy Index (DEI)**: Scores your defensive coverage percentage and pinpoints telemetry blind spots.
3. **Telemetry Integration**: Correlates simulated activity with Linux Auditd, Windows Sysmon (Events 1, 3, 7, 10), and Zeek network logs.
4. **Automated Purple Team Reporting**: Generates markdown and JSON scorecards for immediate SOC tuning.

## Quickstart

```bash
# 1. Clone repository
git clone https://github.com/scorpionxploit/scorpionxploit-redteam-ai.git
cd scorpionxploit-redteam-ai

# 2. Install dependencies
python -m pip install -r requirements.txt

# 3. Generate authorization token
python -m redteam_ai.cli generate-token --target "lab.internal.lan" --secret "YOUR_SECRET_KEY"

# 4. Run benign simulation
python -m redteam_ai.cli simulate --target "lab.internal.lan" --token "<GENERATED_TOKEN>"
```

## Running Tests
```bash
pytest -v tests/
```

## Security & Ethics
Please review [AUDIT.md](AUDIT.md) and [SECURITY.md](SECURITY.md) for full compliance guidelines.
