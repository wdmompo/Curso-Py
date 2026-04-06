# 🧠 El arte de la abstracción: Funciones y el principio DRY

## 📌 Introducción
El desarrollo de software sería altamente ineficiente si tuviéramos que escribir todo desde cero cada vez.  
El **principio DRY (Don't Repeat Yourself)**, popularizado por *Andy Hunt* y *Dave Thomas* en *The Pragmatic Programmer*, junto con las **funciones**, permite construir software de forma eficiente y elegante.

---

## 🔑 Principio DRY: Eficiencia en el código

El principio **DRY** propone eliminar la duplicación de código:

- Consolidar lógica repetida en un único bloque reutilizable
- Reducir errores e inconsistencias
- Simplificar el mantenimiento

### 🛒 Ejemplo
En una plataforma de e-commerce, sin DRY:
- Código duplicado para descuentos, pagos y emails

Con DRY:
```python
def calculate_discount(price, discount_percentage):
    return price * (1 - discount_percentage)
```

- 👉 Una sola función = fuente única de verdad


### 🧩 Funciones: Base del código modular

Las funciones son unidades de código que realizan tareas específicas.

Actúan como “verbos”:

- calcular_area
- validar_direccion
- enviar_email


### 📝 Ejemplo: Calcular el área de un rectángulo
```python
def calculate_area(length, width):
    area = length * width
    return area

# Uso
rectangle_area = calculate_area(5, 3)
print(f"The area of the rectangle is: {rectangle_area}")
```

### 🥣 Argumentos (Entradas)

- length, width
- Son los datos que recibe la función

### 🍽️ Valor de retorno (Salida)

- area
- Resultado devuelto al programa

### 🧠 Filosofía modular

Las funciones convierten un programa en una colección de bloques independientes y reutilizables.

## 🤝 DRY + Funciones

Las funciones son la mejor forma de aplicar DRY:

- Evitan repetir código
- Mejoran organización
- Facilitan pruebas y depuración

### 🎁 Beneficios de la reutilización

- Código más mantenible
- Menos errores
- Mayor productividad

### 📈 Escalabilidad

- Divide problemas grandes en partes pequeñas
- Facilita agregar nuevas funcionalidades

### 🔧 Mantenibilidad

- Cambios localizados
- Menos riesgo de errores

### 👥 Trabajo en equipo

- Código modular
- Desarrollo en paralelo

### 🧪 Pruebas

- Permiten pruebas unitarias
- Aíslan errores fácilmente

### 📖 Legibilidad

- Código más claro y estructurado

### 🐞 Depuración

- Errores localizados en funciones específicas

## 🔄 Refactorización

La refactorización consiste en mejorar el código sin cambiar su comportamiento.

### 🛒 Ejemplo

Antes:

Cálculo de impuestos repetido en varias partes

Después:

```python
def calculate_final_price(price, tax_rate):
    return price * (1 + tax_rate)
```

- 👉 Un solo cambio afecta todo el sistema

## ⚖️ DRY vs Simplicidad

DRY no debe aplicarse en exceso.

❌ Problema:

Demasiadas funciones → código complejo

✅ Equilibrio:

- Código claro, simple y reutilizable

## 📌 Cuándo crear funciones
- Uso frecuente
- Alta complejidad
- Probabilidad de cambio

## 🧰 Funciones en Python moderno

### 🎭 Decoradores

Modifican funciones sin cambiar su lógica

### 🔄 Generadores

Producen datos bajo demanda (eficientes en memoria)

🧵 F-strings

Formateo de texto más claro:

```python
f"Hola, {name}"
```

## 🏷️ Tipado

```python
def calculate_area(length: float, width: float) -> float:
```

## 🌍 Uso en el mundo real

Las funciones permiten:

- Procesar datos
- Entrenar modelos de machine learning
- Trabajar con APIs y bases de datos

👉 Aíslan la lógica y facilitan cambios

## 🧠 Conclusión

El principio DRY y las funciones permiten:

- Código limpio y reutilizable
- Sistemas escalables
- Trabajo colaborativo eficiente

Son herramientas clave para cualquier desarrollador moderno de Python.

