# config.py

import os
from dotenv import load_dotenv

load_dotenv()  # Load isi file .env ke environment

ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")
