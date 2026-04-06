# Clases en Python

## 📌 ¿Qué es una clase?
Una **clase** es un plano o plantilla (blueprint) utilizado para crear objetos.

Define:
- **Atributos** (datos)
- **Métodos** (funciones)

Las clases permiten crear múltiples objetos con características y comportamientos definidos.

---

## 🚗 Analogía
- **Clase** → Plano de un automóvil  
- **Objeto** → Cada auto producido en la fábrica  

---

## 🎯 Propósito de las clases

Las clases ayudan a:
- Organizar el código
- Reutilizar lógica
- Extender funcionalidades

Se basan en tres conceptos clave:

---

## 🔑 Principios fundamentales

### 1. Encapsulación
Agrupa datos y funciones en una sola unidad.

- Mejora la organización
- Promueve modularidad

---

### 2. Herencia
Permite que una clase herede atributos y métodos de otra.

- Facilita reutilización
- Crea jerarquías

**Ejemplo:**
- Clase base: `Vehículo`
- Subclases: `Camión`, `Motocicleta`

---

### 3. Polimorfismo
Permite que diferentes clases respondan de forma distinta a la misma operación.

**Ejemplo:**
Método `dibujar()` en:
- Círculo
- Cuadrado
- Triángulo  

Cada uno se comporta de manera diferente.

---

## 🧩 Componentes de una clase

### 1. Atributos
Variables que almacenan datos del objeto.

**Ejemplo:**
- color
- número de asientos

---

### 2. Métodos
Funciones que definen comportamientos.

**Ejemplo:**
- acelerar()
- frenar()

---

### 3. Constructor
Método especial que se ejecuta al crear un objeto.

- Inicializa atributos
- Se define con `__init__`

---

## 🏗️ Ejemplo de estructura

```python
class NombreClase:
    
    def __init__(self, parametros):
        self.atributo = parametros
    
    def metodo(self):
        # acción
        pass
```

## ⚙️ Instanciación

La instanciación es el proceso de crear un objeto a partir de una clase.

```
objeto = NombreClase(valor)
```

### 💳 Ejemplo práctico: Cuenta bancaria

```python
class BankAccount:
    
    def __init__(self, name, balance, account_number):
        self.name = name
        self.balance = balance
        self.account_number = account_number
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount

# Instanciación
alice_account = BankAccount("Alice", 1000, "12345")
```

-  🌍 Aplicaciones reales

🏪 Gestión de inventario

Clase Producto:
- Atributos: nombre, precio, stock
- Métodos: actualizar stock, generar reportes

🎮 Desarrollo de videojuegos

Clase Personaje:
 - Atributos: salud, fuerza, posición
 - Métodos: atacar, moverse, recibir daño

## 🧠 Conclusión

Las clases son esenciales en Python para:

- Modelar entidades del mundo real
- Crear sistemas complejos
- Escribir código organizado y reutilizable

Dominar clases es clave para avanzar en programación orientada a objetos.


### Cuál de los siguientes escenarios demostraría el concepto de polimorfismo en las clases de Python? Seleccione la mejor respuesta.

- [ ] Una clase Customer con atributos como name y email, y un método send_email que envía un correo electrónico personalizado al cliente.
- [x] Una clase Vehicle con subclases como Car y Motorcycle que comparten los métodos de Vehicle y añaden los suyos propios.
- [ ] Una clase BankAccount con métodos para deposit y withdraw, donde el atributo balance se actualiza en función de la transacción.
- [ ] Una clase Product con atributos como name y price, utilizada para crear una lista de productos en un sistema de inventario.

> Correcto Ilustra el polimorfismo, ya que diferentes subclases (Coche, Motocicleta) responden al mismo mensaje (accelerate()) de formas distintas, reflejando sus características únicas.