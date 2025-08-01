from flask import Flask, request, jsonify
from flask_cors import CORS
from blockchain.chain import Blockchain
from wallet.wallet import QuantumWallet
from transaction.transaction import Transaction
import uuid
import traceback

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

blockchain = Blockchain()
wallets = {}  # {wallet_name: (QuantumWallet, address)}


@app.route("/wallet/create", methods=["POST"])
def create_wallet():
    data = request.get_json()
    name = data.get("name")

    if not name:
        return jsonify({"error": "Wallet name is required"}), 400

    wallet = QuantumWallet(name)
    address = wallet.create_new_address(name)
    wallets[name] = (wallet, address)

    return jsonify({"address": address})


@app.route("/wallet/balance/name/<wallet_name>", methods=["GET"])
def get_balance_by_name(wallet_name):
    if wallet_name not in wallets:
        return jsonify({"error": "Wallet not found"}), 404
    _, address = wallets[wallet_name]
    balance = blockchain.get_balance(address)
    return jsonify({"balance": balance})


@app.route("/transaction/send", methods=["POST"])
def send_transaction():
    data = request.get_json()
    sender_name = data.get("sender")       # Name, not address
    recipient_name = data.get("recipient") # Name, not address
    amount = data.get("amount")

    if not all([sender_name, recipient_name, amount]):
        return jsonify({"error": "Missing fields"}), 400

    if sender_name not in wallets:
        return jsonify({"error": f"Sender wallet '{sender_name}' not found"}), 404
    sender_wallet, sender_address = wallets[sender_name]

    if recipient_name not in wallets:
        return jsonify({"error": f"Recipient wallet '{recipient_name}' not found"}), 404
    _, recipient_address = wallets[recipient_name]

    try:
        amount = float(amount)
        tx = sender_wallet.send_transaction(recipient_address, amount, sender_address)

        tx_dict = tx.to_dict()

        print("--- Transaction Debug Info ---")
        print("TX Dict:", tx_dict)

        is_valid = blockchain.validate_transaction(tx_dict)
        print("Validation result:", is_valid)

        if not is_valid:
            raise ValueError("validate_transaction() returned False")

        result = blockchain.add_transaction(tx_dict)
        if result:
            return jsonify({"message": "Transaction added", "tx_id": tx.transaction_id}), 201
        else:
            return jsonify({"error": "Transaction validation failed"}), 400
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


@app.route("/mine", methods=["POST"])
def mine_block():
    data = request.get_json()
    miner_name = data.get("miner_address")  # it's actually a name

    if not miner_name:
        return jsonify({"error": "Miner name required"}), 400

    if miner_name not in wallets:
        return jsonify({"error": "Miner wallet not found"}), 404

    _, miner_address = wallets[miner_name]  # extract real address
    block = blockchain.mine_block(miner_address)
    return jsonify(block)


@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = [block.to_dict() for block in blockchain.chain]
    return jsonify({
        'length': len(chain_data),
        'chain': chain_data
    }), 200



@app.route("/wallets", methods=["GET"])
def list_wallets():
    return jsonify({
        "wallets": [
            {"name": name, "address": addr}
            for name, (_, addr) in wallets.items()
        ]
    })


@app.route("/transactions/pending", methods=["GET"])
def get_pending_transactions():
    return jsonify({
        "pending_transactions": blockchain.current_transactions
    })


if __name__ == "__main__":
    app.run(port=5000, debug=True)
