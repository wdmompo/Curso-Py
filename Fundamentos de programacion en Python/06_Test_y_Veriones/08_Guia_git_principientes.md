# Git para Principiantes

## Resumen en puntos clave

### 1. ¿Qué es Git?

Git es un sistema de control de versiones que permite:

- Guardar el historial completo de un proyecto.
- Recuperar versiones anteriores del código.
- Experimentar sin riesgo.
- Colaborar con otros desarrolladores.
- Mantener un registro detallado de los cambios.

### Analogía

Git funciona como una **máquina del tiempo para tu código**:

```text
Versión 1 → Versión 2 → Versión 3 → Versión 4
                ↑
          Puedes volver aquí
```

Si introduces un error, puedes regresar a una versión anterior fácilmente.

---

# ¿Por qué es importante Git?

## 2. Control de versiones

Git registra cada cambio realizado en el proyecto.

### Permite

- Comparar versiones.
- Detectar cuándo apareció un error.
- Recuperar trabajo perdido.
- Auditar modificaciones.

### Beneficios

✅ Mayor seguridad.

✅ Mejor mantenimiento.

✅ Desarrollo más confiable.

---

## 3. Colaboración

Git facilita el trabajo en equipo.

### Antes

```text
archivo_final.py
archivo_final_v2.py
archivo_final_definitivo.py
archivo_final_definitivo_ahora_si.py
```

### Con Git

```text
Repositorio compartido
        │
 ┌──────┼──────┐
 │      │      │
Dev A  Dev B  Dev C
```

Todos trabajan sobre el mismo proyecto de forma organizada.

---

## 4. Experimentación segura

Git permite probar ideas sin afectar el proyecto principal.

### Ejemplo

```text
main
 │
 └── nueva-funcionalidad
```

Si algo sale mal:

- Se elimina la rama.
- El proyecto principal permanece intacto.

---

## 5. Estándar de la industria

Git es utilizado por:

- Empresas tecnológicas.
- Proyectos Open Source.
- Equipos de desarrollo.
- Startups y grandes corporaciones.

Aprender Git mejora significativamente el perfil profesional de un desarrollador.

---

# Conceptos fundamentales

## 6. Repositorio (Repository)

Es el contenedor donde Git almacena:

- Código fuente.
- Historial de cambios.
- Configuración del proyecto.

### Representación

```text
Proyecto
│
├── app.py
├── requirements.txt
└── .git/
```

La carpeta `.git` contiene toda la información de control de versiones.

---

## 7. Commit

Un commit es una instantánea del proyecto en un momento determinado.

### Contiene

- Cambios realizados.
- Autor.
- Fecha.
- Mensaje descriptivo.

### Ejemplo

```text
Commit A
 ↓
Commit B
 ↓
Commit C
```

### Crear un commit

```bash
git commit -m "Agrega validación de usuarios"
```

---

## 8. Branch (Rama)

Una rama es una línea de desarrollo independiente.

### Ejemplo

```text
main
 │
 ├── Commit A
 ├── Commit B
 │
 └── feature-login
      ├── Commit C
      └── Commit D
```

### Ventajas

- Desarrollo paralelo.
- Correcciones aisladas.
- Menos riesgos.

---

## 9. Merge (Fusión)

Permite combinar cambios de una rama en otra.

### Ejemplo

```text
main
 │
 ├── A
 │
 └── feature-login
      ├── B
      └── C

            ↓ merge

main
 │
 ├── A
 ├── B
 └── C
```

---

## 10. Push y Pull

### Push

Envía cambios locales al repositorio remoto.

```bash
git push
```

### Pull

Obtiene los cambios más recientes del repositorio remoto.

```bash
git pull
```

---

# Flujo de trabajo típico en Git

## Paso 1: Inicializar un repositorio

```bash
git init
```

Crea la carpeta oculta:

```text
.git/
```

---

## Paso 2: Modificar archivos

Ejemplo:

```python
print("Hola Git")
```

---

## Paso 3: Agregar archivos al área de preparación

```bash
git add .
```

o

```bash
git add app.py
```

---

## Paso 4: Crear un commit

```bash
git commit -m "Primer commit"
```

---

## Paso 5: Crear una rama

```bash
git branch nueva-funcionalidad
```

---

## Paso 6: Cambiar de rama

```bash
git checkout nueva-funcionalidad
```

O en versiones modernas:

```bash
git switch nueva-funcionalidad
```

---

## Paso 7: Seguir desarrollando

```text
Modificar
 ↓
git add
 ↓
git commit
```

---

## Paso 8: Fusionar cambios

```bash
git merge nueva-funcionalidad
```

---

## Paso 9: Subir cambios al repositorio remoto

```bash
git push
```

---

## Paso 10: Obtener cambios de otros desarrolladores

```bash
git pull
```

---

# Desafíos comunes para principiantes

## 11. Curva de aprendizaje

Al principio pueden resultar difíciles conceptos como:

- Commit.
- Branch.
- Merge.
- Repositorio.

### Consejo

Aprende primero:

```text
git init
git add
git commit
git push
git pull
```

Luego avanza hacia ramas y fusiones.

---

## 12. Practicar es fundamental

La mejor forma de aprender Git es usándolo.

### Recomendación

Crear un repositorio de prueba:

```bash
mkdir git-practica
cd git-practica

git init
```

Y experimentar libremente.

---

## 13. Buscar ayuda cuando sea necesario

Recursos útiles:

- Documentación oficial.
- Tutoriales.
- Videos.
- Foros.
- Stack Overflow.

Nadie aprende Git sin cometer errores.

---

## 14. Línea de comandos vs Interfaces gráficas

### Interfaces gráficas (GUI)

Más fáciles para comenzar.

Ejemplos:

- GitHub Desktop
- Sourcetree
- GitKraken

### Línea de comandos

Más potente y flexible.

```bash
git status
git log
git branch
git merge
```

Con el tiempo se convierte en la herramienta preferida de muchos desarrolladores.

---

# Mentalidad Git

Git no es sólo una herramienta.

Es una forma de trabajar basada en:

- Historial de cambios.
- Experimentación segura.
- Colaboración.
- Organización.
- Recuperación ante errores.

### Filosofía Git

```text
Probar
 ↓
Guardar
 ↓
Experimentar
 ↓
Fusionar
 ↓
Mejorar
```

Sin miedo a perder trabajo.

---

# Buenas prácticas

✅ Hacer commits frecuentes.

✅ Escribir mensajes claros.

✅ Crear ramas para nuevas funcionalidades.

✅ Mantener la rama principal estable.

✅ Hacer pull regularmente.

✅ Subir cambios mediante push.

✅ Probar antes de fusionar.

✅ No trabajar directamente en producción.

---

# Comandos esenciales

| Comando | Descripción |
|----------|-------------|
| `git init` | Inicializa un repositorio |
| `git status` | Muestra el estado actual |
| `git add` | Agrega archivos al área de preparación |
| `git commit` | Guarda cambios |
| `git branch` | Crea o lista ramas |
| `git checkout` | Cambia de rama |
| `git switch` | Alternativa moderna a checkout |
| `git merge` | Fusiona ramas |
| `git push` | Envía cambios al remoto |
| `git pull` | Descarga cambios del remoto |
| `git log` | Muestra historial de commits |

---

# Conclusión

Git es una herramienta esencial para cualquier desarrollador porque permite:

- Controlar versiones del código.
- Recuperar cambios fácilmente.
- Trabajar en equipo.
- Experimentar sin riesgos.
- Mantener un historial completo del proyecto.

Aunque puede parecer complejo al principio, dominar Git proporciona una base sólida para el desarrollo profesional y se convierte rápidamente en una de las herramientas más valiosas del flujo de trabajo de cualquier programador.