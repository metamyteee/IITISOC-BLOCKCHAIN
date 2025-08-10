import hashlib
import json
import datetime
from typing import List, Dict, Any, Optional
from blockchain.block import Block
from crypto.pqcrypto import verify_signature

class Blockchain:
    def __init__(self):
        self.chain: List[Block] = []
        self.current_transactions: List[Dict[str, Any]] = []
        self.mining_reward = 10.0
        self.difficulty = 5
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(
            index=1,
            transactions=[],
            proof=1,
            previous_hash='0'
        )
        self.chain.append(genesis_block)

    def get_previous_block(self) -> Optional[Block]:
        return self.chain[-1] if self.chain else None

    def add_transaction(self, transaction: Dict[str, Any]) -> int:
        if self.validate_transaction(transaction):
            self.current_transactions.append(transaction)
            return self.get_previous_block().index + 1
        else:
            raise ValueError("Invalid transaction")

    def validate_transaction(self, tx: Dict[str, Any]) -> bool:
        required_fields = ['sender', 'recipient', 'amount', 'signature', 'timestamp', 'transaction_id']
        for field in required_fields:
            if field not in tx:
                print(f"[❌] Missing field in transaction: {field}")
                return False

        if tx['sender'] == 'System':
            return True

        try:
            message = f"{tx['sender']}{tx['recipient']}{tx['amount']}{tx['timestamp']}"
            signature = tx['signature']
            pubkeys = tx.get('sender_public_key', {})

            if not all(k in signature for k in ('dilithium_signature', 'ecdsa_signature')):
                print("[❌] Signature keys missing")
                return False

            if not all(k in pubkeys for k in ('dilithium_public', 'ecdsa_public')):
                print("[❌] Public keys missing")
                return False

            result = verify_signature(
                message,
                signature['dilithium_signature'],
                signature['ecdsa_signature'],
                pubkeys['dilithium_public'],
                pubkeys['ecdsa_public']
            )

            print(f"[DEBUG] Signature verification result: {result}")
            return result

        except Exception as e:
            print(f"[❌] Error in signature verification: {str(e)}")
            return False

    def proof_of_work(self, previous_proof: int) -> int:
        new_proof = 1
        while not self.valid_proof(previous_proof, new_proof):
            new_proof += 1
        return new_proof

    def valid_proof(self, previous_proof: int, proof: int) -> bool:
        guess = f'{previous_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:self.difficulty] == "0" * self.difficulty

    def mine_block(self, miner_address: str) -> Dict[str, Any]:
        reward_transaction = {
            'sender': 'System',
            'recipient': "MinerWallet",
            'amount': self.mining_reward,
            'signature': 'mining_reward',
            'timestamp': str(datetime.datetime.now()),
            'transaction_id': 'reward'
        }
        self.current_transactions.append(reward_transaction)

        previous_block = self.get_previous_block()
        proof = self.proof_of_work(previous_block.proof)
        new_block = Block(
            index=len(self.chain) + 1,
            transactions=self.current_transactions.copy(),
            proof=proof,
            previous_hash=previous_block.compute_hash()
        )

        self.current_transactions = []
        self.chain.append(new_block)
        return new_block.to_dict()

    def is_chain_valid(self, chain: List[Block]) -> bool:
        if not chain:
            return False

        for i in range(1, len(chain)):
            prev = chain[i - 1]
            curr = chain[i]

            if curr.previous_hash != prev.compute_hash():
                return False

            if not self.valid_proof(prev.proof, curr.proof):
                return False

            for tx in curr.transactions:
                if not self.validate_transaction(tx):
                    return False

        return True

    def get_balance(self, address: str) -> float:
        balance = 0.0
        for block in self.chain:
            for tx in block.transactions:
                try:
                    amount = float(tx['amount'])
                    if tx['sender'] == address:
                        balance -= amount
                    if tx['recipient'] == address:
                        balance += amount
                except Exception:
                    continue
        return round(balance, 2)
