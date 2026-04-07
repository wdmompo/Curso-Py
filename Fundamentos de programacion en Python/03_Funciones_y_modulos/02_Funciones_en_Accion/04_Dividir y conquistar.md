# Dividir y conquistar: el poder de la modularidad

## 🧩 Ideas principales

- **Modularidad en Python**: consiste en dividir el código en funciones pequeñas y reutilizables, cada una con una tarea específica.
- **Ventajas**:
  - Mejora la legibilidad del código.
  - Facilita la reutilización.
  - Permite detectar y corregir errores más fácilmente.
  - Favorece el trabajo en equipo.

---

## ⚙️ Valores por defecto

- Permiten que una función tenga parámetros opcionales con valores predefinidos.
- Hacen el código más flexible y fácil de usar.

```python
def calculate_area(width=1, height=1):
    area = width * height
    return area

Ejemplos:

calculate_area()        # 1
calculate_area(5, 3)    # 15
⚠️ Cuidado con argumentos mutables
Los valores por defecto se evalúan una sola vez.
Usar listas o diccionarios como valores por defecto puede causar errores.

Buena práctica:

def func(lista=None):
    if lista is None:
        lista = []
🎯 Parámetros opcionales
Algunos parámetros son obligatorios, otros opcionales.
def greet(name, greeting="Hello"):
    print(greeting, name)

Ejemplos:

greet("Alice")                  # Hello Alice
greet("Bob", "Good morning")    # Good morning Bob
🔑 Argumentos con palabras clave
Permiten especificar claramente qué valor corresponde a cada parámetro.
greet(name="David", greeting="Salutations")
🔄 Número variable de argumentos
*args: argumentos posicionales (tupla)
**kwargs: argumentos con nombre (diccionario)
def flexible_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

flexible_function(1, 2, 3, name="Alice", age=30)
🧠 Buenas prácticas
Usar nombres claros y descriptivos.
Elegir valores por defecto adecuados.
Documentar funciones con docstrings.
Mantener el código simple y reutilizable.
🧪 Ejemplo completo
def create_user_profile(name, age, occupation="Student", interests=None):
    """
    Crea un perfil de usuario con intereses opcionales.
    """
    if interests is None:
        interests = []

    profile = {
        "name": name,
        "age": age,
        "occupation": occupation
    }

    if interests:
        profile["interests"] = interests

    return profile
🥪 Reto: función make_sandwich
✅ Implementación
def make_sandwich(bread_type, filling, cheese="ninguno", toasted=False):
    sandwich = f"Hacer un sándwich de {bread_type}"

    if toasted:
        sandwich += " tostado"

    sandwich += f" con {filling}"

    if cheese != "ninguno":
        sandwich += f" y queso {cheese}"

    sandwich += "."

    return sandwich
📌 Ejemplos
make_sandwich("trigo", "pavo", "cheddar", True)
# Hacer un sándwich de trigo tostado con pavo y queso cheddar.

make_sandwich("centeno", "jamón")
# Hacer un sándwich de centeno con jamón.