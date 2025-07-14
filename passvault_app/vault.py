import json
import os
from rich.table import Table
from rich.console import Console

VAULT_FILE = "vault.json.enc"
console = Console()

def load_vault(cipher) -> dict:
    if not os.path.exists(VAULT_FILE):
        return {}

    try:
        with open(VAULT_FILE, "rb") as file:
            encrypted = file.read()
        decrypted = cipher.decrypt(encrypted)
        return json.loads(decrypted)
    except Exception:
        console.print("[red]❌ Vault file corrupted or wrong master key.[/red]")
        return {}

def save_vault(data: dict, cipher) -> None:
    try:
        encrypted = cipher.encrypt(json.dumps(data).encode())
        with open(VAULT_FILE, "wb") as file:
            file.write(encrypted)
    except Exception as e:
        console.print(f"[red]Error saving vault:[/red] {e}")

def add_password(vault: dict, service: str, username: str, password: str) -> None:
    vault[service] = {
        "username": username,
        "password": password
    }

def display_passwords(vault: dict) -> None:
    if not vault:
        console.print("[yellow]⚠️ Vault is empty.[/yellow]")
        return

    table = Table(title="🔐 Stored Passwords", show_lines=True)
    table.add_column("Service", style="cyan", no_wrap=True)
    table.add_column("Username")
    table.add_column("Password")

    for service, info in vault.items():
        table.add_row(service, info["username"], info["password"])

    console.print(table)

def remove_password(vault: dict, service: str) -> bool:
    """
    Removes a password entry from the vault by service name.

    Args:
        vault (dict): Existing vault data.
        service (str): Service name to remove.

    Returns:
        bool: True if the entry was removed, False otherwise.
    """
    if service in vault:
        del vault[service]
        return True
    return False