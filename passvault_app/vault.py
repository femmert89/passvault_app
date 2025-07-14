import json
import os
from rich.table import Table
from rich.console import Console

VAULT_FILE = "vault.json.enc"
console = Console()

def load_vault(cipher) -> dict:
    """
    Intenta cargar el archivo cifrado del vault y devolver los datos desencriptados.

    Args:
        cipher (Fernet): Objeto de cifrado Fernet para descifrar.

    Returns:
        dict: Diccionario con los datos del vault o vacío si no existe o falla.
    """
     
    if not os.path.exists(VAULT_FILE):
        return {}

    try:
        with open(VAULT_FILE, "rb") as file:
            encrypted = file.read()
        decrypted = cipher.decrypt(encrypted)
        return json.loads(decrypted)
    except Exception:
        console.print("[red]Vault file corrupted or wrong master key.[/red]")
        return {}

def save_vault(data: dict, cipher) -> None:
    """
    Guarda el vault cifrado en el archivo local.

    Args:
        vault (dict): Diccionario con los datos a guardar.
        cipher (Fernet): Objeto Fernet usado para cifrar los datos.
    """
     
    try:
        encrypted = cipher.encrypt(json.dumps(data).encode())
        with open(VAULT_FILE, "wb") as file:
            file.write(encrypted)
    except Exception as e:
        console.print(f"[red]Error saving vault:[/red] {e}")

def add_password(vault: dict, service: str, username: str, password: str) -> None:
    """
    Agrega una nueva entrada de contraseña al vault.

    Args:
        vault (dict): Diccionario actual del vault.
        service (str): Nombre del servicio (e.g., Gmail).
        username (str): Usuario asociado.
        password (str): Contraseña del usuario.
    """
    vault[service] = {
        "username": username,
        "password": password
    }

def display_passwords(vault: dict) -> None:
    """
    Muestra todas las contraseñas guardadas en formato de tabla.

    Args:
        vault (dict): Diccionario con las entradas del vault.
    """
    if not vault:
        console.print("[yellow]Vault is empty.[/yellow]")
        return

    table = Table(title="Stored Passwords", show_lines=True)
    table.add_column("Service", style="cyan", no_wrap=True)
    table.add_column("Username")
    table.add_column("Password")

    for service, info in vault.items():
        table.add_row(service, info["username"], info["password"])

    console.print(table)

def remove_password(vault: dict, service: str) -> bool:
    """
    Elimina una entrada específica del vault por nombre de servicio.

    Args:
        vault (dict): Diccionario del vault.
        service (str): Nombre del servicio a eliminar.

    Returns:
        bool: True si se eliminó, False si no se encontró.
    """
    if service in vault:
        del vault[service]
        return True
    return False