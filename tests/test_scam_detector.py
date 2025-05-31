# tests/test_scam_detector.py
import pytest
from scam_detector import analyze_contract_code

def test_analyze_contract_code_safe():
    safe_code = """
    function transfer(address to, uint256 amount) public returns (bool) {
        // valid transfer code
    }
    """
    warnings = analyze_contract_code(safe_code)
    assert warnings == []

def test_analyze_contract_code_honeypot():
    bad_code = "function transfer() public { revert('honeypot'); }"
    warnings = analyze_contract_code(bad_code)
    assert any("honeypot" in w.lower() for w in warnings)

def test_analyze_contract_code_no_transfer():
    no_transfer_code = "pragma solidity ^0.8.0; contract Token {}"
    warnings = analyze_contract_code(no_transfer_code)
    assert any("transfer" in w.lower() for w in warnings)
