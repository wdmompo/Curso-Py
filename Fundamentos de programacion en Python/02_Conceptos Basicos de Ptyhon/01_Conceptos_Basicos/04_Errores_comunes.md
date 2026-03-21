# Errores comunes en la ejecución de código en Python

## 🧠 Idea principal
Python es un lenguaje poderoso y fácil de usar, pero durante la ejecución del código pueden surgir errores comunes. Comprender cómo funciona el intérprete y evitar estos errores permite escribir código más eficiente, fiable y libre de fallos.

---

## ⚙️ Cómo funciona la ejecución del código en Python
- El intérprete de Python ejecuta el código **línea por línea**.
- Analiza cada instrucción, la traduce y luego la ejecuta.
- Este proceso secuencial es clave para entender muchos errores.

---

## ❌ Errores comunes y cómo evitarlos

### 1. Errores de sangría (indentación)
- Python usa la sangría para definir bloques de código.
- Una mala indentación provoca errores o comportamientos inesperados.

✅ **Solución:**
- Mantener una indentación consistente.
- Usar editores que ayuden visualmente.

---

### 2. Ámbito de las variables
- Las variables solo existen dentro del bloque donde se definen.

✅ **Solución:**
- Definir variables en el ámbito adecuado.
- Usar variables globales con moderación.

---

### 3. Valores inmutables
- Las cadenas (`strings`) no se pueden modificar directamente.

❌ Incorrecto:
```python
value = "Hello"
value[0] = 'h'
print(value)
```

- Una solucion usando Slice

```python
value = "Hello"
new_value = "h" + value[1:]
print(new_value)
```

- Otra solucion usando `replace()`

```python
value = "Hello"
new_value = value.replace("Hello", "hello")
print(new_value)
```

✅ Correcto:
```python
value = "Hello"
value = value.lower()
print(value)
```
### 4. Reasignación de variables

- Reutilizar nombres de variables puede sobrescribir valores sin querer.

#### ✅ Solución:

- Usar nombres claros y diferentes para evitar confusión.

### 5. No manejar excepciones

Errores como dividir por cero detienen el programa.

#### ❌ Ejemplo:

```python
result = x / y
```

#### ✅ Solución con manejo de errores:

```python
try:
    result = x / y
except ZeroDivisionError:
    print("Error: Division by zero")
```

## 🚀 Conceptos avanzados y buenas prácticas

### 🔁 Importaciones circulares

- Ocurren cuando dos módulos dependen entre sí.
- Generan bucles difíciles de resolver.

### 🧮 Gestión de memoria

Uso ineficiente puede causar fallos o consumo excesivo.

#### ❌ Ejemplo peligroso:

````python
my_string = ""
lots_of_as = "a" * 1000000000
while True:
    my_string = my_string + lots_of_as  # Add 1 billion "a" characters
```

## 🧪 Pruebas y depuración

- Es fundamental probar el código regularmente.
- A medida que el software crece, las pruebas manuales no son suficientes.

## ✅ Recomendación:

- Usar pruebas automatizadas.
- Aprovechar herramientas de depuración.

## 🎯 Conclusión

- Comprender estos errores comunes y cómo evitarlos te permitirá:
- Escribir código más limpio y eficiente.
- Reducir fallos inesperados.
- Mejorar tu capacidad como programador.
