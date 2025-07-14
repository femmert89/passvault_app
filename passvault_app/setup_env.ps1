# setup_env.ps1 – prepara el entorno en Windows

# 1. Crear el virtualenv
python -m venv .venv

# 2. Activar
.\.venv\Scripts\Activate.ps1

# 3. Instalar dependencias
pip install -r requirements.txt

Write-Host "Entorno listo. Ejecuta: python main.py"