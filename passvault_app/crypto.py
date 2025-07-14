import base64
import hashlib
from cryptography.fernet import Fernet

def get_cipher(master_key: str) -> Fernet:
    hashed = hashlib.sha256(master_key.encode()).digest()
    b64_key = base64.urlsafe_b64encode(hashed)
    return Fernet(b64_key)