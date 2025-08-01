import json
import datetime
from typing import Dict, Any
from crypto.pqcrypto import sign_message, verify_signature

class Transaction:
    def __init__(self, sender: str, recipient: str, amount: float, sender_public_key: Dict[str, str] = None, signature: Dict[str, str] = None):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.sender_public_key = sender_public_key
        self.signature = signature
        self.timestamp = str(datetime.datetime.now())
        self.transaction_id = self.generate_transaction_id()

    def generate_transaction_id(self) -> str:
        import hashlib
        data = f"{self.sender}{self.recipient}{self.amount}{self.timestamp}"
        return hashlib.sha256(data.encode()).hexdigest()

    def to_dict(self) -> Dict:
     return {
        'sender': self.sender,
        'recipient': self.recipient,
        'amount': self.amount,
        'timestamp': self.timestamp,
        'transaction_id': self.transaction_id,
        'signature': self.signature,
        'sender_public_key': self.sender_public_key  # ✅ this was missing
    }


    def serialize(self) -> str:
        return f"{self.sender}{self.recipient}{self.amount}{self.timestamp}"

    def sign_transaction(self, d_priv: str, e_priv: str):
        message = self.serialize()
        self.signature = sign_message(message, d_priv, e_priv)

    def verify_signature(self) -> bool:
        if not self.signature or not self.sender_public_key:
            return False

        message = self.serialize()
        return verify_signature(
            message,
            self.signature['dilithium_signature'],
            self.signature['ecdsa_signature'],
            self.sender_public_key['dilithium_public'],
            self.sender_public_key['ecdsa_public']
        )

    def is_valid(self) -> bool:
        return self.amount > 0 and self.sender and self.recipient and (self.sender == 'System' or self.verify_signature())