# blockchain/block.py

import hashlib
import json
import datetime
from typing import List, Dict

class Block:
    def __init__(self, index: int, transactions: List[Dict], proof: int, previous_hash: str, timestamp: str = None):
        self.index = index
        self.timestamp = timestamp or str(datetime.datetime.now())
        self.transactions = transactions
        self.proof = proof
        self.previous_hash = previous_hash
        self.merkle_root = self.calculate_merkle_root()

    def calculate_merkle_root(self) -> str:
        if not self.transactions:
            return hashlib.sha256(b'').hexdigest()
        
        hashes = [
            hashlib.sha256(json.dumps(tx, sort_keys=True).encode()).hexdigest()
            for tx in self.transactions
        ]
        
        while len(hashes) > 1:
            if len(hashes) % 2 == 1:
                hashes.append(hashes[-1])
            hashes = [
                hashlib.sha256((hashes[i] + hashes[i+1]).encode()).hexdigest()
                for i in range(0, len(hashes), 2)
            ]
        return hashes[0]

    def to_dict(self) -> Dict:
        return {
            'index': self.index,
            'timestamp': self.timestamp,
            'transactions': self.transactions,
            'proof': self.proof,
            'previous_hash': self.previous_hash,
            'merkle_root': self.merkle_root
        }

    def compute_hash(self) -> str:
        """
        Returns the SHA-256 hash of the block's contents (used in block validation).
        """
        block_string = json.dumps(self.to_dict(), sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
