# INF-8239 — Unidad 01: Entorno Reproducible

## Sistema Operativo
- Windows 11
- PowerShell (terminal utilizada para todo el proceso)

## Herramientas y versiones
- Python: 3.13.5
- Git: 2.55.0.windows.5

## Estructura del proyecto

## Pasos ejecutados

### 1. Configuracion de Git
```powershell
git config --global user.name "Johanna Joaquin"
git config --global user.email "lic.jjoaquin@gmail.com"
```

### 2. Configuracion de SSH con GitHub
```powershell
ssh-keygen -t ed25519 -C "lic.jjoaquin@gmail.com"
Set-Service -Name ssh-agent -StartupType Manual
Start-Service ssh-agent
ssh-add C:\Users\yoany\.ssh\id_ed25519
ssh -T git@github.com
```

### 3. Creacion del entorno virtual
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 4. Instalacion de dependencias
```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 5. Modulo y prueba
Se creo el modulo inf8239_u01 con la funcion environment_message() y su prueba correspondiente en tests/test_environment.py.

Ejecucion de la prueba:
```powershell
$env:PYTHONPATH="src"
python -m pytest -q
```
**Resultado:** 1 passed

### 6. Verificacion de Jupyter
Se creo el notebook notebooks/00_verificacion.ipynb, conectado al kernel .venv (Python 3.13.5), confirmando que el interprete usado corresponde al entorno virtual del proyecto.

### 7. Control de versiones
```powershell
git init
git add .
git commit -m "chore: create INF-8239 reproducible environment"
```
**Resultado:** working tree clean y commit visible con git log --oneline.

## Evidencias
- [x] Versiones de Python y Git
- [x] Ruta del interprete .venv desde el notebook
- [x] Salida 1 passed de pytest
- [x] Arbol de carpetas del proyecto
- [x] git log --oneline con el primer commit
- [x] Este README con sistema operativo y comandos usados
