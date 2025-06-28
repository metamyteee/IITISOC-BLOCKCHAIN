import datetime
import hashlib
import json

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash='0')  # Genesis block

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False

        while not check_proof:
            hash_operation = hashlib.sha256(
                str(new_proof**2 - previous_proof**2).encode()
            ).hexdigest()
            if hash_operation[:5] == '00000':
                check_proof = True
            else:
                new_proof += 1

        return new_proof

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1

        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False

            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(
                str(proof**2 - previous_proof**2).encode()
            ).hexdigest()

            if hash_operation[:5] != '00000':
                return False
            previous_block = block
            block_index += 1

        return True
add this file in blockchain/block.py


import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from crypto.pqcrypto import generate_keys, sign_message, verify_signature, public_key_to_address

class TestPQCrypto(unittest.TestCase):
    def test_key_generation(self):
        """Test quantum-resistant key generation"""
        public_key, private_key = generate_keys()
        
        self.assertIsInstance(public_key, str)
        self.assertIsInstance(private_key, str)
        self.assertNotEqual(public_key, private_key)
        self.assertGreater(len(public_key), 0)
        self.assertGreater(len(private_key), 0)
    
    def test_signing_and_verification(self):
        """Test quantum-resistant signing and verification"""
        public_key, private_key = generate_keys()
        message = b"Hello, quantum world!"
        
        
        signature = sign_message(message, private_key)
        self.assertIsInstance(signature, str)
        
        
        is_valid = verify_signature(message, signature, public_key)
        self.assertTrue(is_valid)
        
        
        wrong_message = b"Wrong message"
        is_valid_wrong = verify_signature(wrong_message, signature, public_key)
        self.assertFalse(is_valid_wrong)
    
    def test_address_generation(self):
        """Test address generation from public key"""
        public_key, _ = generate_keys()
        address = public_key_to_address(public_key)
        
        self.assertIsInstance(address, str)
        self.assertEqual(len(address), 40)  
    
    def test_signature_with_different_keys(self):
        """Test that signature fails with different keys"""
        pub1, priv1 = generate_keys()
        pub2, priv2 = generate_keys()
        
        message = b"Test message"
        signature = sign_message(message, priv1)
        
        
        self.assertTrue(verify_signature(message, signature, pub1))
        
        
        self.assertFalse(verify_signature(message, signature, pub2))

if __name__ == '__main__':
    unittest.main()

