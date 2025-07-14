from rich import print
from rich.console import Console
from crypto import get_cipher
from vault import (load_vault, save_vault, add_password, display_passwords, remove_password)

console = Console()

def main():
    print("[bold cyan]\nWelcome to passvault_app[/bold cyan]")
    master_key = console.input("Insert your [yellow]master key[/yellow]: ")

    cipher = get_cipher(master_key)
    vault = load_vault(cipher)

    while True:
        print("\n[bold white]Main Menu[/bold white]")
        print("[green]1)[/green] Add new password")
        print("[green]2)[/green] Delete password")
        print("[green]3)[/green] Show all")
        print("[green]4)[/green] Exit")

        choice = console.input("\nSelect an option: ")

        if choice == '1':
            service = console.input("Service (e.g., Gmail): ")
            username = console.input("User: ")
            password = console.input("Password: ")

            add_password(vault, service, username, password)
            save_vault(vault, cipher)
            print("[green]Password saved successfully[/green]")

        elif choice == '2':
            service = console.input("Service name to delete: ")
            confirm = console.input(f"Delete entry for '{service}'? (y/n): ")

            if confirm.lower() == 'y':
                success = remove_password(vault, service)
                if success:
                    save_vault(vault, cipher)
                    print("[green]Entry deleted successfully.[/green]")
                else:
                    print("[yellow]Service not found in vault.[/yellow]")
            else:
                print("[blue]Deletion cancelled.[/blue]")

        elif choice == '3':
            display_passwords(vault)

        elif choice == '4':
            print("[bold red]Exiting password manager...[/bold red]")
            break

        else:
            print("[red]Invalid option. Please try again.[/red]")

if __name__ == "__main__":
    main()