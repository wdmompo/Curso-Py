# 🔁 Introducción a los Bucles y Sentencias Condicionales

La programación frecuentemente requiere **repetir acciones** o **tomar decisiones** según ciertas condiciones. Para ello se utilizan dos herramientas fundamentales:

- 🔁 **Bucles** → para repetir código  
- 🔀 **Sentencias condicionales** → para tomar decisiones  

---

## 🔹 Bucles: El poder de la repetición

Los bucles permiten ejecutar un bloque de código múltiples veces sin repetir instrucciones manualmente.

### Tipos principales en Python:

### 📌 Bucle `for` (iteración sobre secuencias)

Se utiliza cuando se conoce el número de repeticiones o se trabaja con colecciones.

```python
for i in range(1, 11):
  print(i)
```
- range(1, 11) genera números del 1 al 10
- i toma cada valor y ejecuta print(i)

✔️ Ideal para:

- Listas
- Tuplas
- Cadenas
- Secuencias en general

## 📌 Bucle while (basado en condición)

Se ejecuta mientras una condición sea verdadera.

```python 
valid_input = False

while not valid_input:
  user_input = int(input("Please enter a number greater than 0: "))
  if user_input > 0:
    valid_input = True
  else:
    print("Invalid input. Please try again.")
```


✔️ Útil cuando:

- No se conoce el número de iteraciones
- Se espera una condición específica (ej: entrada válida)## 

## ✅ Ventajas de los bucles

- Reducen duplicación de código
- ejoran legibilidad y mantenimiento
- ermiten iterar estructuras de datos
- Automatizan tareas repetitivas

🔹 Sentencias condicionales: Toma de decisiones

Permiten ejecutar diferentes bloques de código según una condición.

📌 Estructura if-else
```python
player_score = 80

if player_score > 100:
  print("Congratulations! You scored over 100 points.")
else:
  print("Keep trying to beat your high score!")
```

✔️ Permite:

- Controlar el flujo del programa
- Adaptarse a entradas del usuario
- Implementar reglas lógicas

## 🌍 Aplicaciones reales

📊 Análisis de datos → recorrer datos y filtrar información
🌐 Desarrollo web → contenido dinámico y autenticación
🎮 Videojuegos → lógica del juego y comportamiento
🤖 Aprendizaje automático → entrenamiento de modelos

## ⚠️ Problemas comunes y buenas prácticas

❌ Evitar:

- Bucles demasiado anidados
- Condiciones complejas e ilegibles
- Bucles infinitos

## ✅ Recomendaciones:

- Mantener bucles simples
- Usar condiciones claras
- Dividir problemas complejos

Considerar alternativas (listas por comprensión, funciones lambda)

### 🎯 Desafío: Adivina el número secreto

✔️ Objetivo:

Crear un programa donde la computadora adivine un número entre 1 y 10.

💡 Solución:

```python
import random

# Número secreto definido manualmente
secret_number = 7

# Inicializar variable
guess = 0

# Bucle hasta acertar
while guess != secret_number:
  guess = random.randint(1, 10)
  print("Guessing:", guess)

print("I guessed the right number! It was", secret_number)
```

## ✅ Conclusión

Los bucles y las sentencias condicionales:

- Automatizan procesos
- Permiten lógica dinámica
- Son esenciales en cualquier programa

# 🔁 Tipos de Bucles y Uso Avanzado en Python

## 🔹 Importancia de los bucles
Los bucles permiten ejecutar instrucciones repetidamente (**iteración**), evitando código redundante y mejorando:

- ✅ Eficiencia  
- ✅ Mantenimiento del código  
- ✅ Colaboración entre desarrolladores  

---

## 🔹 Tipos de bucles en Python

### 📌 Bucle `for`

Se utiliza para iterar sobre secuencias como listas, tuplas, cadenas o rangos.

```python
for i in range(start, end):
    # Código a ejecutar
🔸 Ejemplo:
for i in range(1, 11):
    print(i)
```

✔️ Imprime números del 1 al 10 (el límite final no se incluye).

### 📌 Uso de range()

- range(stop) → de 0 a stop-1
- range(start, stop) → de start a stop-1
- range(start, stop, step) → con incrementos personalizados

Ejemplo:

- range(1, 10, 2)  # 1, 3, 5, 7, 9

## 📌 Bucle while

Ejecuta código mientras una condición sea verdadera.

while condition:
    # Código a ejecutar

🔸 Ejemplo:

```python
number = 1
while number <= 10:
    print(number)
    number = number + 1
```

✔️ Más flexible cuando no se conoce el número de iteraciones.

## 🔹 Listas y bucles

📌 Definición de lista:

```python
fruits = ["apple", "banana", "cherry"]
```

📌 Acceso por índice:

```python
first_fruit = fruits[0]
```

📌 Longitud de lista:

```python
len(fruits)
```

📌 Añadir elementos:

```python
fruits.append("date")
```

🔹 Iteración sobre listas

✔️ Forma recomendada (for each):

```python
students = ["Alice", "Bob", "Charlie"]

for student in students:
    print("Hello,", student)
````

❗ Alternativa menos limpia:

```
for i in range(0, len(students)):
    print("Hello,", students[i])
```


🔹 Ejemplos prácticos

🎲 Simulación con while

```python
import random

roll = 0
while roll != 6:
    roll = random.randint(1, 6)
    print("You rolled a", roll)
➕ Suma de números
total = 0
for number in range(1, 101):
    total += number

print("The sum is:", total)
```

🔍 Filtrar números pares

```
numbers = [1, 2, 3, 4, 5]
index = 0

while index < len(numbers):
    if numbers[index] % 2 == 0:
        print(numbers[index])
    index += 1
```

🔹 Bucles anidados

Permiten trabajar con estructuras más complejas.

📌 Ejemplo: tabla de multiplicar

```
for i in range(1, 11):
    for j in range(1, 11):
        print(i, "*", j, "=", i * j, end="\t")
    print()
```

🎯 Desafío: Números divisibles por 3 y 4
✔️ Solución:
max_value = 50

```  
for number in range(max_value + 1):
    if number % 3 == 0 and number % 4 == 0:
        print(number)
```

✔️ Salida esperada:

0
12
24
36
48

## ✅ Buenas prácticas

- ✔️ Usar for cuando se conocen iteraciones
- ✔️ Usar while para condiciones dinámicas
- ✔️ Evitar bucles muy complejos o anidados
- ✔️ Usar nombres descriptivos
- ✔️ Mantener buena indentación
- ✔️ Optimizar cálculos dentro del bucle

🧠 Conclusión

Los bucles for y while:

- Automatizan tareas repetitivas
- Facilitan el procesamiento de datos
- Permiten crear programas eficientes y escalables

👉 Dominar su uso es esencial para escribir código claro, potente y mantenible.