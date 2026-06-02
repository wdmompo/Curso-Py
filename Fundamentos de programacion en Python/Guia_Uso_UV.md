# Guía completa de uso de `uv` en Python


## 1. ¿Qué es `uv`?
`uv` es una herramienta moderna para gestionar entornos, instalar paquetes y acelerar la gestión de dependencias en proyectos Python. Es multiplataforma y puede usarse como gestor de versiones de Python, instalador de paquetes, acelerador de `pip`, y mucho más.

---


## 2. Instalación de `uv`

### macOS y Linux
```sh
curl -Ls https://astral.sh/uv/install.sh | sh
# O usando Homebrew (macOS):
brew install astral-sh/uv/uv
```

### Windows
Ejecuta en PowerShell:
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

> **Tip:**
> También puedes instalar uv con pip, Homebrew y otros métodos. Consulta la [página de instalación](https://astral.sh/uv/) para más detalles.


---

## 3. Gestión de proyectos y entornos con `uv`

`uv` permite gestionar dependencias y entornos de proyectos, soportando lockfiles, workspaces y más (similar a rye o poetry):

```sh
uv init ejemplo
cd ejemplo
uv add ruff
uv run ruff check
uv lock
uv sync
```

También puedes construir y publicar proyectos, incluso si no están gestionados con uv. Consulta la guía de empaquetado para más información.

---

## 4. Gestión de scripts con `uv`

`uv` gestiona dependencias y entornos para scripts de un solo archivo:

```sh
echo 'import requests; print(requests.get("https://astral.sh"))' > ejemplo.py
uv add --script ejemplo.py requests
uv run ejemplo.py
```

---

## 5. Herramientas de línea de comandos con `uv`

Ejecuta herramientas en entornos efímeros usando `uvx` (alias de `uv tool run`):

```sh
uvx pycowsay 'hola mundo!'
```

Instala herramientas globalmente:
```sh
uv tool install ruff
ruff --version
```

---

## 6. Manejo de versiones de Python

Instala y cambia rápidamente entre versiones de Python:

```sh
uv python install 3.10 3.11 3.12
uv venv --python 3.12.0
uv run --python pypy@3.8 -- python
uv python pin 3.11
```

---

## 7. Interfaz pip acelerada

`uv` provee un reemplazo rápido para los comandos comunes de pip, pip-tools y virtualenv:

```sh
uv pip install -r requirements.txt
uv pip install numpy
uv pip install --upgrade -r requirements.txt
uv pip compile requirements.in --universal --output-file requirements.txt
uv venv
uv pip sync requirements.txt
```

Puedes migrar a uv sin cambiar tus flujos de trabajo existentes y obtener una aceleración de 10-100x en la instalación de dependencias.

---

## 3. Uso de `uv` como instalador de paquetes y acelerador de `pip`

### Instalación de paquetes en un entorno existente
- Instalar dependencias desde `requirements.txt`:
  ```sh
  uv pip install -r requirements.txt
  ```
- Instalar un paquete específico:
  ```sh
  uv pip install numpy
  ```
- Actualizar paquetes:
  ```sh
  uv pip install --upgrade -r requirements.txt
  ```


> **Nota:** No es necesario crear un entorno con `uv venv` para usar `uv pip`. Puedes usarlo en cualquier entorno virtual ya creado (por ejemplo, con `python -m venv` o `conda`).

---


---

## 8. Crear alias para agilizar el uso


### PowerShell (Windows)
Agrega en tu perfil de PowerShell (`$PROFILE`):
```powershell
Set-Alias upi "uv pip install"
Set-Alias upir "uv pip install -r requirements.txt"
```

### CMD (Windows, usando batch)
Crea un archivo `uv_alias.bat` en una carpeta de tu `PATH`:
```bat
@echo off
if "%1"=="install" (
  uv pip install %2 %3 %4 %5 %6 %7 %8 %9
) else (
  uv %*
)
```

### Bash (Linux/macOS)
Agrega en tu `~/.bashrc` o `~/.zshrc`:
```sh
alias upi='uv pip install'
alias upir='uv pip install -r requirements.txt'
```

---


---

## 9. Recursos
- Documentación oficial: https://github.com/astral-sh/uv
- Instalación y releases: https://astral.sh/uv/

---

> **Resumen:**
> - Usa `uv` para instalar y gestionar versiones de Python en cualquier SO.
> - Usa `uv pip` para instalar dependencias más rápido en cualquier entorno.
> - Puedes crear alias para simplificar comandos frecuentes.
> - uv permite gestionar proyectos, scripts, herramientas y versiones de Python de forma rápida y moderna.
