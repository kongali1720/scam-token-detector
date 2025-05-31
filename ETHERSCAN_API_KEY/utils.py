# utils.py

import requests
from config import ETHERSCAN_API_KEY

def is_verified_on_etherscan(contract_address):
    url = f"https://api.etherscan.io/api"
    params = {
        "module": "contract",
        "action": "getsourcecode",
        "address": contract_address,
        "apikey": ETHERSCAN_API_KEY
    }

    try:
        res = requests.get(url, params=params, timeout=10)
        data = res.json()
        if data["status"] == "1":
            source_code = data["result"][0]["SourceCode"]
            is_verified = bool(source_code.strip())
            contract_name = data["result"][0]["ContractName"]
            return is_verified, contract_name
        else:
            return False, "Unknown"
    except Exception as e:
        print(f"[ERROR] Etherscan check failed: {e}")
        return False, "Error"
