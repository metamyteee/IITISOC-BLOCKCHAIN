import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from transaction.transaction import Transaction, TransactionPool
from crypto.pqcrypto import generate_keys

class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.public_key, self.private_key = generate_keys()
        self.sender_address = "sender123"
        self.recipient_address = "recipient456"
    
    def test_transaction_creation(self):
        """Test transaction creation"""
        tx = Transaction(
            sender=self.sender_address,
            recipient=self.recipient_address,
            amount=25.0,
            sender_public_key=self.public_key
        )
        
        self.assertEqual(tx.sender, self.sender_address)
        self.assertEqual(tx.recipient, self.recipient_address)
        self.assertEqual(tx.amount, 25.0)
        self.assertIsNotNone(tx.transaction_id)
        self.assertIsNotNone(tx.timestamp)
    
    def test_transaction_signing(self):
        """Test transaction signing and verification"""
        tx = Transaction(
            sender=self.sender_address,
            recipient=self.recipient_address,
            amount=15.0,
            sender_public_key=self.public_key
        )
        
        
        tx.sign_transaction(self.private_key)
        self.assertIsNotNone(tx.signature)
        
        
        self.assertTrue(tx.verify_signature())
    
    def test_transaction_validation(self):
        """Test transaction validation"""
        
        tx = Transaction(
            sender=self.sender_address,
            recipient=self.recipient_address,
            amount=10.0,
            sender_public_key=self.public_key
        )
        tx.sign_transaction(self.private_key)
        self.assertTrue(tx.is_valid())
        
        
        invalid_tx = Transaction(
            sender=self.sender_address,
            recipient=self.recipient_address,
            amount=-5.0
        )
        self.assertFalse(invalid_tx.is_valid())
    
    def test_transaction_pool(self):
        """Test transaction pool operations"""
        pool = TransactionPool()
        
        
        tx = Transaction(
            sender=self.sender_address,
            recipient=self.recipient_address,
            amount=20.0,
            sender_public_key=self.public_key
        )
        tx.sign_transaction(self.private_key)
        
        
        self.assertTrue(pool.add_transaction(tx))
        self.assertEqual(len(pool.pending_transactions), 1)
        
        
        transactions = pool.get_transactions()
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0].transaction_id, tx.transaction_id)

if __name__ == '__main__':
    unittest.main()