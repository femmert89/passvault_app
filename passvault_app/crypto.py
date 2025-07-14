import base64
import hashlib
from cryptography.fernet import Fernet

def get_cipher(master_key: str) -> Fernet:
    
    """
    Genera un objeto de cifrado Fernet a partir de una clave maestra.

    Args:
        master_key (str): Clave proporcionada por el usuario.

    Returns:
        Fernet: Objeto de cifrado para encriptar y desencriptar datos.
    """
      
    hashed = hashlib.sha256(master_key.encode()).digest()
    b64_key = base64.urlsafe_b64encode(hashed)
    return Fernet(b64_key)