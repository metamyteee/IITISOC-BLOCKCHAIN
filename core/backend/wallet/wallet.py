import os
import json
from typing import Dict
from crypto.pqcrypto import generate_keys, sign_message, verify_signature, public_key_to_address
from transaction.transaction import Transaction

class QuantumWallet:
    def __init__(self, wallet_name: str):
        self.wallet_name = wallet_name
        self.addresses: Dict[str, Dict[str, str]] = {}
        self.wallet_dir = os.path.join("wallet", "data", wallet_name)
        os.makedirs(self.wallet_dir, exist_ok=True)
        self._load_wallet()

    def _wallet_file(self):
        return os.path.join(self.wallet_dir, "keys.json")

    def _load_wallet(self):
        try:
            with open(self._wallet_file(), "r") as f:
                self.addresses = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.addresses = {}

    def _save_wallet(self):
        with open(self._wallet_file(), "w") as f:
            json.dump(self.addresses, f, indent=4)

    def create_new_address(self, label: str) -> str:
        keys = generate_keys()
        self.addresses[label] = keys
        self._save_wallet()
        return public_key_to_address(keys["dilithium_public"])

    def get_address_by_label(self, label: str) -> str:
        if label in self.addresses:
            return public_key_to_address(self.addresses[label]["dilithium_public"])
        raise ValueError(f"Label '{label}' not found")

    def get_keys_by_address(self, address: str):
        for label, keys in self.addresses.items():
            if public_key_to_address(keys["dilithium_public"]) == address:
                return keys
        raise ValueError("Address not found")

    def send_transaction(self, recipient_address: str, amount: float, sender_address: str) -> Transaction:
        keys = self.get_keys_by_address(sender_address)
        tx = Transaction(
            sender=sender_address,
            recipient=recipient_address,
            amount=amount,
            sender_public_key={
                "dilithium_public": keys["dilithium_public"],
                "ecdsa_public": keys["ecdsa_public"]
            }
        )
        tx.sign_transaction(keys["dilithium_private"], keys["ecdsa_private"])

        if not tx.verify_signature():
            raise ValueError("Signature verification failed")
        return tx
