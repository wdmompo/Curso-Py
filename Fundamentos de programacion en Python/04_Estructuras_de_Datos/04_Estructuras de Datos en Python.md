# Estructuras de Datos en Python

## Introducción

Cuando trabajas en aplicaciones con muchos datos, organizarlos correctamente es fundamental para mantener el código rápido, limpio y fácil de mantener.

Las estructuras de datos ayudan a:

- Organizar información
- Acceder a datos eficientemente
- Mejorar el rendimiento
- Simplificar el desarrollo

Elegir la estructura correcta es como usar la herramienta adecuada para cada trabajo.

---

# ¿Qué son las Estructuras de Datos?

Las estructuras de datos son formas de organizar y almacenar información.

Cada estructura está diseñada para resolver diferentes necesidades.

---

# Tipos Principales

## Las estructuras más comunes en Python son:

- Listas (`list`)
- Diccionarios (`dict`)
- Conjuntos (`set`)

---

# Listas (`list`)

## ¿Qué son?

Las listas almacenan colecciones ordenadas de elementos.

Se utilizan cuando:

- El orden importa
- Necesitas modificar elementos
- Quieres recorrer datos secuencialmente

---

# Ejemplo de Lista

```python
pasos_receta = [
    "Cortar verduras",
    "Hervir agua",
    "Agregar sal"
]
```

---

# Características de las Listas

Las listas:

- Mantienen el orden
- Permiten duplicados
- Son modificables

---

# Casos de Uso

## Ejemplos reales

- Pasos de una receta
- Niveles de un videojuego
- Flujo de usuarios
- Historial de navegación

---

# Agregar Elementos

```python
pasos_receta.append("Servir comida")
```

---

# Diccionarios (`dict`)

## ¿Qué son?

Los diccionarios almacenan información usando pares:

```python
clave -> valor
```

Son ideales para relacionar datos.

---

# Ejemplo de Diccionario

```python
usuarios = {
    "charlie": "contraseña123",
    "ana": "abc456"
}
```

---

# Características de los Diccionarios

Los diccionarios:

- Permiten búsquedas rápidas
- Relacionan información
- Usan claves únicas

---

# Casos de Uso

## Ejemplos reales

- Usuarios y contraseñas
- Configuración de aplicaciones
- Bases de datos
- Perfiles de usuario

---

# Acceder a Datos

```python
print(usuarios["charlie"])
```

---

# Agregar Información

```python
usuarios["lucia"] = "pass789"
```

---

# Conjuntos (`set`)

## ¿Qué son?

Los conjuntos almacenan elementos únicos.

No permiten duplicados.

---

# Ejemplo de Set

```python
powerups = {
    "velocidad",
    "escudo",
    "doble_salto"
}
```

---

# Características de los Sets

Los sets:

- Eliminan duplicados automáticamente
- Son rápidos para búsquedas
- No mantienen orden

---

# Casos de Uso

## Ejemplos reales

- Visitantes únicos de un sitio web
- Palabras únicas en un documento
- Clases de personajes
- Etiquetas o hashtags únicos

---

# Evitar Duplicados

```python
powerups.add("velocidad")
```

El elemento no se duplicará.

---

# Comparación de Estructuras

| Estructura | Orden | Duplicados | Uso principal |
|---|---|---|---|
| Lista (`list`) | Sí | Sí | Secuencias ordenadas |
| Diccionario (`dict`) | Sí | Claves únicas | Relacionar información |
| Set (`set`) | No | No | Elementos únicos |

---

# Ejemplo Completo

## Aplicación simple

```python
# Lista
flujo_usuarios = [
    "inicio",
    "registro",
    "perfil"
]

# Diccionario
perfiles = {
    "usuario1": {
        "nombre": "Carlos",
        "edad": 25
    }
}

# Set
caracteristicas = {
    "chat",
    "perfil",
    "estadisticas"
}
```

---

# Beneficios de Elegir la Estructura Correcta

## Ventajas

- Mejor rendimiento
- Código más claro
- Mayor organización
- Acceso eficiente a datos
- Escalabilidad

---

# Idea Principal

La estructura de datos adecuada puede transformar completamente una aplicación.

La clave es entender:

- Qué tipo de datos tienes
- Cómo necesitas acceder a ellos
- Qué operaciones realizarás con frecuencia

Cada estructura resuelve problemas diferentes y todas trabajan juntas para construir aplicaciones eficientes.