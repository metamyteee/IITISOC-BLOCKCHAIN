import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from blockchain.chain import Blockchain
from transaction.transaction import Transaction

class TestBlockchain(unittest.TestCase):
    def setUp(self):
        self.blockchain = Blockchain()
    
    def test_genesis_block(self):
        """Test genesis block creation"""
        self.assertEqual(len(self.blockchain.chain), 1)
        self.assertEqual(self.blockchain.chain[0]['index'], 1)
        self.assertEqual(self.blockchain.chain[0]['previous_hash'], '0')
    
    def test_add_transaction(self):
        """Test adding valid transaction"""
        tx = Transaction("Alice", "Bob", 10.0)
        tx_dict = tx.to_dict()
        tx_dict['sender_public_key'] = 'test_key'
        tx_dict['signature'] = 'test_signature'
        
        
        original_validate = self.blockchain.validate_transaction
        self.blockchain.validate_transaction = lambda x: True
        
        result = self.blockchain.add_transaction(tx_dict)
        self.assertIsNotNone(result)
        self.assertEqual(len(self.blockchain.current_transactions), 1)
        
       
        self.blockchain.validate_transaction = original_validate
    
    def test_mining(self):
        """Test block mining"""
        initial_length = len(self.blockchain.chain)
        miner_address = "miner123"
        
        block = self.blockchain.mine_block(miner_address)
        
        self.assertEqual(len(self.blockchain.chain), initial_length + 1)
        self.assertEqual(block['index'], initial_length + 1)
        self.assertTrue(any(tx['recipient'] == miner_address for tx in block['transactions']))
    
    def test_chain_validation(self):
        """Test blockchain validation"""
       
        self.assertTrue(self.blockchain.is_chain_valid(self.blockchain.chain))
        
        
        self.blockchain.mine_block("miner1")
        self.blockchain.mine_block("miner2")
        
       
        self.assertTrue(self.blockchain.is_chain_valid(self.blockchain.chain))
    
    def test_balance_calculation(self):
        """Test balance calculation"""
        address = "test_address"
        
       
        self.assertEqual(self.blockchain.get_balance(address), 0.0)
        
        
        self.blockchain.mine_block(address)
        
        
        self.assertEqual(self.blockchain.get_balance(address), self.blockchain.mining_reward)

if __name__ == '__main__':
    unittest.main()