# Configuración de Git: Guía para Principiantes

## Resumen en puntos clave

### 1. ¿Qué es Git?

Git es un **Sistema de Control de Versiones Distribuido (DVCS)** que permite:

- Rastrear cambios en el código.
- Colaborar con otros desarrolladores.
- Recuperar versiones anteriores.
- Gestionar proyectos de forma segura.

### Ventaja principal

Cada desarrollador posee una copia completa del repositorio:

```text
Repositorio Completo
       │
 ┌─────┼─────┐
 │     │     │
Dev A Dev B Dev C
```

Esto proporciona:

✅ Trabajo sin conexión.

✅ Mayor seguridad.

✅ Mejor tolerancia a fallos.

---

# Requisitos previos

Antes de instalar Git necesitas:

## Sistema operativo compatible

- Windows
- macOS
- Linux

## Conexión a Internet

Necesaria para:

- Clonar repositorios.
- Subir cambios.
- Colaborar con otros desarrolladores.

---

# Instalación de Git

## Paso 1: Descargar Git

Descargar desde:

```text
https://git-scm.com/
```

Seleccionar la versión adecuada para tu sistema operativo.

---

## Paso 2: Instalar Git

Seguir el asistente de instalación.

En la mayoría de los casos:

```text
Siguiente → Siguiente → Instalar
```

es suficiente.

---

## Paso 3: Verificar la instalación

Abrir:

### Windows

```text
Git Bash
```

### macOS

```text
Terminal
```

Ejecutar:

```bash
git --version
```

Resultado esperado:

```bash
git version 2.x.x
```

Si no funciona:

- Reiniciar la terminal.
- Reiniciar el equipo.
- Verificar que Git esté agregado al PATH.

---

# Configuración inicial de Git

## Configurar nombre de usuario

```bash
git config --global user.name "Tu Nombre"
```

Ejemplo:

```bash
git config --global user.name "Juan Perez"
```

---

## Configurar correo electrónico

```bash
git config --global user.email "correo@ejemplo.com"
```

Ejemplo:

```bash
git config --global user.email "juan@gmail.com"
```

---

## Verificar configuración

```bash
git config --list
```

Ejemplo:

```text
user.name=Juan Perez
user.email=juan@gmail.com
```

---

# Crear un repositorio Git

## Inicializar un repositorio

Ubicarse dentro del proyecto:

```bash
cd mi_proyecto
```

Crear repositorio:

```bash
git init
```

Resultado:

```text
.git/
```

Git crea una carpeta oculta que almacenará:

- Historial.
- Configuración.
- Commits.
- Ramas.

---

# Registrar cambios

## Área de preparación (Staging Area)

Antes de guardar cambios, Git utiliza una zona intermedia llamada **staging area**.

### Agregar un archivo

```bash
git add archivo.py
```

### Agregar todos los archivos

```bash
git add .
```

---

## Crear un commit

Guardar una instantánea del proyecto:

```bash
git commit -m "Primer commit"
```

### Ejemplo

```bash
git commit -m "Agrega página de inicio"
```

---

## Flujo básico

```text
Modificar archivo
        ↓
git add
        ↓
git commit
```

---

# Trabajando con ramas

## ¿Qué es una rama?

Una rama permite trabajar de forma aislada.

```text
main
 │
 ├── Commit A
 └── Commit B
```

---

## Crear una rama

```bash
git branch nueva-funcionalidad
```

---

## Cambiar a una rama

```bash
git checkout nueva-funcionalidad
```

O utilizando el comando moderno:

```bash
git switch nueva-funcionalidad
```

---

## Ejemplo visual

```text
main
 │
 ├── A
 └── B

feature-login
 │
 ├── C
 └── D
```

La nueva funcionalidad se desarrolla sin afectar la rama principal.

---

# Fusionar ramas

Cuando una funcionalidad está terminada:

```bash
git merge nueva-funcionalidad
```

Git intentará combinar automáticamente los cambios.

---

## Posibles conflictos

Si dos desarrolladores modifican la misma línea:

```text
<<<<<<< HEAD
Código actual
=======
Código nuevo
>>>>>>> branch
```

Será necesario resolver el conflicto manualmente.

---

# Repositorios remotos

Un repositorio remoto se encuentra en servicios como:

- GitHub
- GitLab
- Azure DevOps

---

## Clonar un repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

Ejemplo:

```bash
git clone https://github.com/usuario/proyecto.git
```

---

## Subir cambios

Enviar commits al servidor:

```bash
git push
```

---

## Descargar cambios

Obtener cambios recientes:

```bash
git pull
```

---

# Escenarios reales

## Escenario 1: Proyecto colaborativo

Equipo desarrollando una web para una panadería.

### División del trabajo

```text
Dev A → Página principal
Dev B → Menú
Dev C → Pedidos online
```

Cada integrante trabaja en su propia rama.

Al finalizar:

```bash
git merge
```

Integra todos los cambios.

---

## Escenario 2: Experimentar sin riesgos

Quieres probar un nuevo diseño.

### Solución

Crear una rama:

```text
main
 │
 └── experimento
```

Si funciona:

```bash
git merge experimento
```

Si falla:

```bash
git branch -D experimento
```

El proyecto principal permanece intacto.

---

## Escenario 3: Volver atrás en el tiempo

Se introduce un error crítico.

Git permite regresar a una versión anterior:

```text
Commit A ✓
Commit B ✓
Commit C ❌
```

Volver a:

```text
Commit B
```

Es como una máquina del tiempo para el código.

---

# Desafíos comunes

## Curva de aprendizaje

Puede resultar complejo al principio por conceptos como:

- Repositorios.
- Commits.
- Branches.
- Merge.

### Solución

Aprender gradualmente:

1. `git init`
2. `git add`
3. `git commit`
4. `git push`
5. `git pull`

Luego avanzar hacia ramas y fusiones.

---

## Conflictos de fusión

Aparecen cuando dos personas modifican el mismo código.

### Recomendaciones

- Hacer pull frecuentemente.
- Comunicar cambios importantes.
- Mantener ramas pequeñas.

---

# Buenas prácticas

✅ Realizar commits pequeños y frecuentes.

✅ Escribir mensajes descriptivos.

```bash
git commit -m "Corrige validación de usuarios"
```

❌ Evitar:

```bash
git commit -m "Cambios"
```

---

✅ Crear ramas para nuevas funcionalidades.

```bash
git branch feature-login
```

---

✅ Hacer push regularmente.

```bash
git push
```

---

✅ Actualizar el repositorio local.

```bash
git pull
```

---

✅ Probar antes de fusionar.

---

# Comandos esenciales

| Comando | Función |
|----------|----------|
| `git --version` | Verificar instalación |
| `git config --global user.name` | Configurar nombre |
| `git config --global user.email` | Configurar correo |
| `git config --list` | Ver configuración |
| `git init` | Crear repositorio |
| `git add` | Preparar cambios |
| `git commit` | Guardar cambios |
| `git branch` | Crear/Listar ramas |
| `git checkout` | Cambiar rama |
| `git switch` | Alternativa moderna |
| `git merge` | Fusionar ramas |
| `git clone` | Clonar repositorio |
| `git push` | Subir cambios |
| `git pull` | Descargar cambios |

---

# Conclusión

La configuración inicial de Git es el primer paso para aprovechar todas las ventajas del control de versiones.

Git permite:

- Mantener un historial completo del proyecto.
- Colaborar con otros desarrolladores.
- Experimentar sin riesgos.
- Recuperar versiones anteriores.
- Gestionar proyectos de forma profesional.

Aunque requiere una pequeña curva de aprendizaje, dominar Git mejora significativamente la productividad y es una habilidad esencial para cualquier desarrollador moderno.