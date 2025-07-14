import base64
import hashlib
from cryptography.fernet import Fernet

def get_cipher(master_key: str) -> Fernet:
    """
    Generates a Fernet cipher from the user's master key.

    Args:
        master_key (str): Plain-text master password.

    Returns:
        Fernet: Cipher object to encrypt/decrypt vault contents.
    """
    # Derive 32-byte key using SHA256 and encode to base64
    hashed = hashlib.sha256(master_key.encode()).digest()
    b64_key = base64.urlsafe_b64encode(hashed)
    return Fernet(b64_key)