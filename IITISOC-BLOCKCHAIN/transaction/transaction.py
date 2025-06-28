import json
import datetime
from typing import Dict, Any, Optional
from crypto.pqcrypto import sign_message, verify_signature, public_key_to_address

class Transaction:
    def __init__(self, sender: str, recipient: str, amount: float, 
                 sender_public_key: str = None, signature: str = None):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.sender_public_key = sender_public_key
        self.signature = signature
        self.timestamp = str(datetime.datetime.now())
        self.transaction_id = self.generate_transaction_id()

    def generate_transaction_id(self) -> str:
        """Generate unique transaction ID"""
        import hashlib
        data = f"{self.sender}{self.recipient}{self.amount}{self.timestamp}"
        return hashlib.sha256(data.encode()).hexdigest()

    def to_dict(self) -> Dict[str, Any]:
        """Convert transaction to dictionary"""
        return {
            'transaction_id': self.transaction_id,
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount,
            'sender_public_key': self.sender_public_key,
            'signature': self.signature,
            'timestamp': self.timestamp
        }

    def serialize(self) -> str:
        """Serialize transaction for signing (as string)"""
        data = f"{self.sender}{self.recipient}{self.amount}{self.timestamp}"
        return data

    def sign_transaction(self, private_key_b64: str):
        """Sign transaction with quantum-resistant signature"""
        if not private_key_b64:
            raise ValueError("Private key required for signing")
        
        message = self.serialize()
        self.signature = sign_message(message, private_key_b64)

    def verify_signature(self) -> bool:
        """Verify transaction signature"""
        if not self.signature or not self.sender_public_key:
            return False
        
        message = self.serialize()
        return verify_signature(message, self.signature, self.sender_public_key)

    def is_valid(self) -> bool:
        """Validate transaction"""
        
        if self.amount <= 0:
            return False
        
        if not self.sender or not self.recipient:
            return False
        
        
        if self.sender != 'System':
            return self.verify_signature()
        
        return True

class TransactionPool:
    def __init__(self):
        self.pending_transactions = []

    def add_transaction(self, transaction: Transaction) -> bool:
        """Add transaction to pool if valid"""
        if transaction.is_valid():
            self.pending_transactions.append(transaction)
            return True
        return False

    def get_transactions(self, count: int = None) -> list:
        """Get transactions from pool"""
        if count is None:
            return self.pending_transactions.copy()
        return self.pending_transactions[:count]

    def remove_transaction(self, transaction_id: str):
        """Remove transaction from pool"""
        self.pending_transactions = [
            tx for tx in self.pending_transactions 
            if tx.transaction_id != transaction_id
        ]

    def clear(self):
        """Clear all pending transactions"""
        self.pending_transactions = []
