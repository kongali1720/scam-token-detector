# utils.py
import requests
from config import ETHERSCAN_API_KEY, BSCSCAN_API_KEY, ETHERSCAN_API_URL, BSCSCAN_API_URL

def fetch_contract_source(chain: str, contract_address: str):
    """Ambil source code smart contract dari Etherscan/BscScan API."""
    if chain.lower() == "ethereum":
        api_url = ETHERSCAN_API_URL
        api_key = ETHERSCAN_API_KEY
    elif chain.lower() == "bsc":
        api_url = BSCSCAN_API_URL
        api_key = BSCSCAN_API_KEY
    else:
        raise ValueError("Unsupported blockchain. Use 'ethereum' or 'bsc'.")

    params = {
        "module": "contract",
        "action": "getsourcecode",
        "address": contract_address,
        "apikey": api_key
    }
    response = requests.get(api_url, params=params)
    data = response.json()

    if data["status"] == "1" and data["result"]:
        return data["result"][0]["SourceCode"]
    else:
        return None
