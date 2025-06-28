dilithium_py.dilithium import Dilithium2
import base64
import hashlib

def generate_keys():
    """Generate quantum-resistant key pair using Dilithium2"""

    public_key, private_key = Dilithium2.keygen()
    
    return (
        base64.b64encode(public_key).decode('utf-8'),
        base64.b64encode(private_key).decode('utf-8')
    )

def sign_message(message, private_key_b64):
    """Sign message with quantum-resistant signature"""
    private_key = base64.b64decode(private_key_b64.encode('utf-8'))
    
    message_bytes = message.encode('utf-8') if isinstance(message, str) else message
    
    signature = Dilithium2.sign(private_key, message_bytes)
    
    return base64.b64encode(signature).decode('utf-8')

def verify_signature(message, signature_b64, public_key_b64):
    """Verify quantum-resistant signature"""
    try:
        public_key = base64.b64decode(public_key_b64.encode('utf-8'))
        signature = base64.b64decode(signature_b64.encode('utf-8'))
        

        message_bytes = message.encode('utf-8') if isinstance(message, str) else message
        

        return Dilithium2.verify(public_key, message_bytes, signature)
        
    except Exception as e:
        print(f"Verification error: {e}")
        return False

def public_key_to_address(public_key_b64):
    """Generate blockchain address from public key"""
    public_key = base64.b64decode(public_key_b64.encode('utf-8'))
    return hashlib.sha256(public_key).hexdigest()[:40]
