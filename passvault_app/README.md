# passvault_app – Gestor de Contraseñas Local

**passvault_app** es una aplicación de línea de comandos (CLI) en Python que te permite almacenar contraseñas de forma segura en un archivo cifrado.  
Utiliza cifrado simétrico con Fernet (`cryptography`) y una clave maestra definida por el usuario.  
Toda la información se guarda de forma local, sin conexión a internet ni servidores externos.

---

## Instalación

1. Clona o descarga este repositorio.
2. Ve a la carpeta del proyecto:
   ```bash
   cd passvault_app
3. Ejecuta el script de configuración (solo para Windows PowerShell):
   .\setup_env.ps1
   
   Si usás Linux o macOS:
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

## Inicialización

1. Ejecuta la aplicación:
   ```bash
   python main.py

## Uso

1. Ingresá tu clave maestra. Si ya tenés un archivo vault.json.enc, se intentará descifrar. Si no existe, se creará uno nuevo.

2. Menú disponible:
   - Agregar nueva contraseña por servicio
   - Eliminar contraseñas ya guardadas
   - Mostrar todas las contraseñas guardadas
   - Salir del gestor

