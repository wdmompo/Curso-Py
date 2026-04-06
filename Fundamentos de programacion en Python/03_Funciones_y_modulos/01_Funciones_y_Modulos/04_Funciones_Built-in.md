# 🧰 Funciones Integradas (Built-in) en Python

## 📌 ¿Qué son las funciones integradas?

Las **funciones integradas (built-in)** son herramientas predefinidas en Python diseñadas para realizar tareas comunes.

- Son reutilizables
- Evitan escribir código desde cero
- Simplifican el desarrollo

Python incluye muchas de estas funciones listas para usar.

---

## 🎯 Beneficios principales

### ⚡ 1. Eficiencia
- Eliminan la necesidad de escribir código repetitivo
- Permiten resolver tareas rápidamente

---

### 📖 2. Legibilidad
- Hacen el código más claro y fácil de entender
- Funcionan como documentación implícita

**Ejemplo:**
```python
sorted(lista)
```

👉 Es evidente que se está ordenando una lista

### ✅ 3. Confiabilidad

Están probadas y optimizadas por la comunidad
Reducen errores en comparación con código propio

#### 🔑 Funciones integradas comunes

- 🖨️ print()
  - Muestra información en consola.

  ```python
  print("Hola mundo")
  ```
  - 📌 Uso:
    - Mostrar resultados
    - Dar feedback al usuario
    - Registrar información

- 📏 len()
  - Devuelve la cantidad de elementos en una secuencia.

  ```python
  len("Hola")
  ```
  - 📌 Uso:
    - Contar elementos
    - Validar longitud (ej: contraseñas)    

- ⌨️ input()
  - Solicita datos al usuario.
    ```python
    nombre = input("Ingresa tu nombre: ")
    ```
  - 📌 Uso:
    - Programas interactivos
    - Recolección de datos

- 🧪 type()
  - Indica el tipo de dato.

  ```python
  type(10)
  ```
  - 📌 Uso:
    - Validación de datos
    - Control de lógica
    - Conversión de tipos

## 🔄 Conversión de tipos
🔢 int()
  - Convierte a entero

  ```python
  int("10")
  ```
  - 📌 Uso:
    - Validación de datos
    - Control de lógica
    - Conversión de tipos

🔢 float()
  - Convierte a decimal

  ```python
  float("3.14")
  ```
  - 📌 Uso:
    - Validación de datos
    - Control de lógica
    - Conversión de tipos

🔤 str()
  - Convierte a texto

  ```python
  str(100)
  ```
  - 📌 Uso:
    - Validación de datos
    - Control de lógica
    - Conversión de tipos


## 🧠 Aplicaciones prácticas

- Contar productos en un carrito → len()
- Pedir datos al usuario → input()
- Validar tipos → type()
- Convertir datos → int(), float(), str()
- Mostrar resultados → print()

## 🧪 Actividades sugeridas
  - 🧮 1. Calculadora simple
    - Usar input(), operadores y print()
  - 🔍 2. Validación de datos
    - Usar len() y type()
    - Ejemplo: validar contraseña
  - 🔄 3. Conversión de datos
    - Convertir entrada con int(), float(), str()
    - Realizar operaciones con los datos

## 🧠 Conclusión

Las funciones integradas:

- Aumentan la productividad
- Mejoran la claridad del código
- Garantizan resultados confiables

### Estás trabajando en un script de Python que necesita procesar la entrada del usuario, realizar cálculos y presentar los resultados de forma clara y organizada. ¿Qué combinación de funciones integradas sería la más adecuada para lograr este objetivo? Selecciona la mejor respuesta.

- [x] input(), operadores aritméticos (+, -, *, /), y print()
- [ ] abs(), round(), y sorted()
- [ ] open(), read(), y write()
- [ ] len(), type(), y int(), float(), str()

> Correcto En esta respuesta, input() recoge los datos del usuario, los operadores aritméticos se encargan de los cálculos y print() muestra los resultados organizados, cumpliendo los requisitos del script.no