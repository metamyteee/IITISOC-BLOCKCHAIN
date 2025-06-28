import datetime
import hashlib
import json
from typing import List, Dict, Any, Optional

class Blockchain:
    def __init__(self):
        self.chain: List[Dict[str, Any]] = []
        self.current_transactions: List[Dict[str, Any]] = []
        self.mining_reward = 10.0
        self.difficulty = 5  
        self.create_block(proof=1, previous_hash='0')  

    def create_block(self, proof: int, previous_hash: str) -> Dict[str, Any]:
        """Create a new block and add it to the chain"""
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'transactions': self.current_transactions.copy(),
            'proof': proof,
            'previous_hash': previous_hash,
            'merkle_root': self.calculate_merkle_root(self.current_transactions)
        }
        
        
        self.current_transactions = []
        self.chain.append(block)
        return block

    def get_previous_block(self) -> Optional[Dict[str, Any]]:
        """Get the last block in the chain"""
        return self.chain[-1] if self.chain else None

    def add_transaction(self, transaction: Dict[str, Any]) -> int:
        """Add a transaction to the current transaction pool"""
        if self.validate_transaction(transaction):
            self.current_transactions.append(transaction)
            return self.get_previous_block()['index'] + 1
        else:
            raise ValueError("Invalid transaction")

    def validate_transaction(self, transaction: Dict[str, Any]) -> bool:
        """Validate a transaction including quantum signature verification"""
        required_fields = ['sender', 'recipient', 'amount', 'signature', 'timestamp']
        if not all(field in transaction for field in required_fields):
            return False
        
        
        from crypto.pqcrypto import verify_signature, public_key_to_address
        
        
        if transaction['sender'] != 'System':  
            try:
                
                message_data = f"{transaction['sender']}{transaction['recipient']}{transaction['amount']}{transaction['timestamp']}"
                return verify_signature(
                    message_data.encode(), 
                    transaction['signature'], 
                    transaction.get('sender_public_key', '')
                )
            except:
                return False
        
        return True

    def proof_of_work(self, previous_proof: int) -> int:
        """Find a valid proof for the next block"""
        new_proof = 1
        
        while not self.valid_proof(previous_proof, new_proof):
            new_proof += 1
            
        return new_proof

    def valid_proof(self, previous_proof: int, proof: int) -> bool:
        """Check if proof is valid"""
        guess = f'{previous_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:self.difficulty] == "0" * self.difficulty

    def hash(self, block: Dict[str, Any]) -> str:
        """Create SHA-256 hash of a block"""
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def calculate_merkle_root(self, transactions: List[Dict[str, Any]]) -> str:
        """Calculate Merkle root of transactions for integrity"""
        if not transactions:
            return hashlib.sha256(b'').hexdigest()
        
        transaction_hashes = [
            hashlib.sha256(json.dumps(tx, sort_keys=True).encode()).hexdigest()
            for tx in transactions
        ]
        
        while len(transaction_hashes) > 1:
            if len(transaction_hashes) % 2 != 0:
                transaction_hashes.append(transaction_hashes[-1])
            
            new_hashes = []
            for i in range(0, len(transaction_hashes), 2):
                combined = transaction_hashes[i] + transaction_hashes[i + 1]
                new_hashes.append(hashlib.sha256(combined.encode()).hexdigest())
            
            transaction_hashes = new_hashes
        
        return transaction_hashes[0]

    def is_chain_valid(self, chain: List[Dict[str, Any]]) -> bool:
        """Validate the entire blockchain"""
        if not chain:
            return False
            
        previous_block = chain[0]
        block_index = 1

        while block_index < len(chain):
            block = chain[block_index]
            
            if block['previous_hash'] != self.hash(previous_block):
                return False

            previous_proof = previous_block['proof']
            proof = block['proof']
            
            if not self.valid_proof(previous_proof, proof):
                return False
                
          
            for transaction in block.get('transactions', []):
                if not self.validate_transaction(transaction):
                    return False
                
            previous_block = block
            block_index += 1

        return True

    def get_balance(self, address: str) -> float:
        """Calculate balance for a given address"""
        balance = 0.0
        
        for block in self.chain:
            for transaction in block.get('transactions', []):
                if transaction['sender'] == address:
                    balance -= transaction['amount']
                if transaction['recipient'] == address:
                    balance += transaction['amount']
                    
        return balance

    def mine_block(self, miner_address: str) -> Dict[str, Any]:
        """Mine a new block with quantum-resistant security"""
        reward_transaction = {
            'sender': 'System',
            'recipient': miner_address,
            'amount': self.mining_reward,
            'signature': 'mining_reward',
            'timestamp': str(datetime.datetime.now())
        }
        self.current_transactions.append(reward_transaction)
        
        previous_block = self.get_previous_block()
        previous_proof = previous_block['proof']
        
        proof = self.proof_of_work(previous_proof)
        previous_hash = self.hash(previous_block)
        
        block = self.create_block(proof, previous_hash)
        return block
