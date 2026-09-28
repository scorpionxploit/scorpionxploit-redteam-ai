"""
Test suite for scorpionxploit-redteam-ai
"""
import pytest
import hmac
import hashlib
import time
from redteam_ai.agent import RedTeamEmulationAgent
from redteam_ai.mitre_mapper import MitreAttackGraph

SECRET_KEY = "test_lab_secret_key_1337"
TARGET = "lab.internal.lan"

def generate_valid_token(secret: str, target: str) -> str:
    ts = str(int(time.time()))
    payload = f"{target}:{ts}"
    sig = hmac.new(secret.encode('utf-8'), payload.encode('utf-8'), hashlib.sha256).hexdigest()
    return f"{target}:{ts}:{sig}"

def test_authorization_valid_token():
    agent = RedTeamEmulationAgent(secret_key=SECRET_KEY, authorized_target=TARGET)
    valid_token = generate_valid_token(SECRET_KEY, TARGET)
    assert agent.verify_authorization(valid_token) is True

def test_authorization_invalid_token_rejected():
    agent = RedTeamEmulationAgent(secret_key=SECRET_KEY, authorized_target=TARGET)
    invalid_token = f"{TARGET}:{int(time.time())}:bad_signature_hex"
    assert agent.verify_authorization(invalid_token) is False

def test_unauthorized_run_raises_permission_error():
    agent = RedTeamEmulationAgent(secret_key=SECRET_KEY, authorized_target=TARGET)
    with pytest.raises(PermissionError):
        agent.execute_simulation_run("fake:token:sig")

def test_simulation_execution_flow():
    agent = RedTeamEmulationAgent(secret_key=SECRET_KEY, authorized_target=TARGET)
    valid_token = generate_valid_token(SECRET_KEY, TARGET)
    result = agent.execute_simulation_run(valid_token)
    assert result["status"] == "COMPLETED"
    scorecard = result["scorecard"]
    assert scorecard["total_techniques_simulated"] == 4
    assert scorecard["coverage_score"] == 75.0
    assert "T1071.001" in scorecard["blind_spots"]

def test_mitre_graph_path_synthesis():
    graph = MitreAttackGraph()
    path = graph.compute_optimal_path("T1059", "T1041")
    assert path[0] == "T1059"
    assert path[-1] == "T1041"
    assert "T1003" in path
