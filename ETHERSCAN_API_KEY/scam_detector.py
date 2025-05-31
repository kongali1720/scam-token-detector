# scam_detector.py

from utils import is_verified_on_etherscan

def analyze_token(contract_address):
    result = {}

    # Etherscan Verification Check
    is_verified, contract_name = is_verified_on_etherscan(contract_address)
    result["verified"] = is_verified
    result["contract_name"] = contract_name

    # Blacklist Check
    result["blacklisted"] = contract_address.lower() in get_blacklist()

    # Simple scam analysis (placeholder logic)
    if result["blacklisted"]:
        result["scam"] = True
        result["reason"] = "Token is in known blacklist database."
    elif not result["verified"]:
        result["scam"] = True
        result["reason"] = "Smart contract is not verified on Etherscan."
    else:
        result["scam"] = False
        result["reason"] = "Token appears to be safe."

    return result
