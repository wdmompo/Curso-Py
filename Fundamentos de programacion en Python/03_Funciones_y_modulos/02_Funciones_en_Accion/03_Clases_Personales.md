## 📘 Clases personalizadas en Python (POO)

### 🧩 Concepto clave
- Las **clases** son plantillas para crear objetos.
- Los **objetos** son instancias de una clase con datos y comportamientos propios.

🧠 Analogía:
- Clase → molde de galletas  
- Objeto → galleta creada a partir del molde  

---

## 🔑 Fundamentos de la Programación Orientada a Objetos (POO)

- **Objetos**: entidades con datos y acciones.
- **Clases**: definen atributos y métodos.
- **Encapsulación**: protege los datos dentro del objeto.
- **Abstracción**: oculta detalles innecesarios.
- **Herencia**: permite crear clases a partir de otras.
- **Polimorfismo**: permite usar diferentes objetos de forma similar.

---

## 🎯 ¿Por qué usar clases?

### 📦 Organización
- Agrupan datos y funciones relacionadas.
- Hacen el código más claro y mantenible.

### ♻️ Reutilización
- Permiten crear múltiples objetos sin repetir código.

### 🔒 Encapsulación
- Controlan el acceso a los datos internos.

---

## 🧱 Estructura de una clase

### 1. Definición

```python
class NombreClase:
    pass
```

### 2. Constructor (__init__)

Inicializa atributos al crear un objeto.

### 3. Atributos

Variables que describen al objeto.

### 4. Métodos

Funciones que definen comportamientos.

🧪 Ejemplo: Clase Car

```python
class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.fuel_level = 100

    def start_engine(self):
        print(f"The {self.year} {self.make} {self.model} starts!")

    def accelerate(self):
        print(f"The {self.color} {self.make} speeds up!")
```

## ⚙️ Conceptos avanzados

- 🔁 Herencia
  - Crear clases basadas en otras.
- 🧬 Polimorfismo
  - Mismo método, distinto comportamiento.
- 🧱 Clases abstractas
  - Definen métodos que otras clases deben implementar.

## 🐶 Ejercicio: Clase Dog

### ✅ Implementación

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"¡Guau! Me llamo {self.name} y soy un {self.breed}.")

# Crear instancia
my_dog = Dog("Buddy", "Golden Retriever")

# Llamar al método
my_dog.bark()
```

🎯 Resultado esperado

```bsdh
¡Guau! Me llamo Buddy y soy un Golden Retriever.
```

## 🚀 Conclusión

- Las clases permiten crear código modular, reutilizable y organizado.
- Son objetos esenciales para proyectos grandes y complejos.
- Dominar POO te permite construir aplicaciones más robustas y escalables.
