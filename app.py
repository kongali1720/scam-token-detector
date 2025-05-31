from flask import Flask, render_template, request, jsonify
from scam_detector import detect_scam_token
import json
import os

app = Flask(__name__)

# Load blacklist (sample static, can later be dynamic)
BLACKLIST_PATH = os.path.join("data", "blacklist.json")
if os.path.exists(BLACKLIST_PATH):
    with open(BLACKLIST_PATH, "r") as f:
        BLACKLIST = json.load(f)
else:
    BLACKLIST = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    contract = request.form.get("contract", "").strip()

    if not contract.startswith("0x") or len(contract) != 42:
        return jsonify({"error": "Alamat kontrak tidak valid."})

    if contract in BLACKLIST:
        return jsonify({"scam": True, "message": "Token ini termasuk dalam daftar hitam 🚨"})

    try:
        result = detect_scam_token(contract)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
