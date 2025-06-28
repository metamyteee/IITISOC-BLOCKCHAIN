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

