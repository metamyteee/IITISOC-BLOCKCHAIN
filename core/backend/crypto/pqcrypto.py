import base58
import hashlib
import json
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import InvalidSignature
from dilithium_py.dilithium import Dilithium2

def b58encode(data: bytes) -> str:
    return base58.b58encode(data).decode()

def b58decode(data: str) -> bytes:
    return base58.b58decode(data.encode())

def generate_keys():
    d_pub, d_priv = Dilithium2.keygen()
    ecdsa_priv = ec.generate_private_key(ec.SECP256R1())
    ecdsa_pub = ecdsa_priv.public_key()

    ecdsa_priv_bytes = ecdsa_priv.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    ecdsa_pub_bytes = ecdsa_pub.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return {
        "dilithium_public": b58encode(d_pub),
        "dilithium_private": b58encode(d_priv),
        "ecdsa_public": b58encode(ecdsa_pub_bytes),
        "ecdsa_private": b58encode(ecdsa_priv_bytes)
    }

def sign_message(message: str, d_priv_b58: str, e_priv_b58: str):
    msg_bytes = message.encode()
    d_priv = b58decode(d_priv_b58)
    d_sig = Dilithium2.sign(d_priv, msg_bytes)
    e_priv_bytes = b58decode(e_priv_b58)
    ecdsa_priv = serialization.load_pem_private_key(e_priv_bytes, password=None)
    e_sig = ecdsa_priv.sign(msg_bytes, ec.ECDSA(hashes.SHA256()))

    return {
        "dilithium_signature": b58encode(d_sig),
        "ecdsa_signature": b58encode(e_sig)
    }

def verify_signature(message: str, d_sig_b58, e_sig_b58, d_pub_b58, e_pub_b58):
    msg_bytes = message.encode()
    d_sig = b58decode(d_sig_b58)
    d_pub = b58decode(d_pub_b58)
    d_valid = Dilithium2.verify(d_pub, msg_bytes, d_sig)

    try:
        e_sig = b58decode(e_sig_b58)
        e_pub_bytes = b58decode(e_pub_b58)
        ecdsa_pub = serialization.load_pem_public_key(e_pub_bytes)
        ecdsa_pub.verify(e_sig, msg_bytes, ec.ECDSA(hashes.SHA256()))
        e_valid = True
    except InvalidSignature:
        e_valid = False
    except Exception:
        e_valid = False

    return d_valid and e_valid

def public_key_to_address(d_pub_b58: str) -> str:
    raw = b58decode(d_pub_b58)
    return hashlib.sha256(raw).hexdigest()[:40]