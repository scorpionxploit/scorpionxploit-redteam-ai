"""
MITRE ATT&CK Graph Mapper & Kill-Chain Path Synthesizer
"""
from typing import List, Dict, Set

class MitreAttackGraph:
    """
    Constructs dependency graph of ATT&CK techniques for realistic campaign planning.
    """
    TACTIC_FLOW = [
        "Initial Access",
        "Execution",
        "Persistence",
        "Privilege Escalation",
        "Defense Evasion",
        "Credential Access",
        "Discovery",
        "Lateral Movement",
        "Exfiltration"
    ]

    def __init__(self):
        self.techniques: Dict[str, Dict[str, Any]] = {
            "T1059": {"name": "Command and Scripting Interpreter", "tactic": "Execution", "prereqs": []},
            "T1082": {"name": "System Information Discovery", "tactic": "Discovery", "prereqs": ["T1059"]},
            "T1003": {"name": "OS Credential Dumping", "tactic": "Credential Access", "prereqs": ["T1082"]},
            "T1021": {"name": "Remote Services (SSH/RDP)", "tactic": "Lateral Movement", "prereqs": ["T1003"]},
            "T1041": {"name": "Exfiltration Over C2", "tactic": "Exfiltration", "prereqs": ["T1021"]}
        }

    def compute_optimal_path(self, start_technique: str, target_technique: str) -> List[str]:
        """Calculates prerequisite chain between starting foothold and objective."""
        path = [start_technique]
        curr = start_technique
        all_techs = list(self.techniques.keys())
        if target_technique in all_techs:
            for t in all_techs[all_techs.index(start_technique) + 1 : all_techs.index(target_technique) + 1]:
                path.append(t)
        return path
