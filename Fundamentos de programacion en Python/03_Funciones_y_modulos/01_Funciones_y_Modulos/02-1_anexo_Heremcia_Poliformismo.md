# 🤔 ¿Herencia o Polimorfismo?

## 🧬 Herencia
La **herencia** ocurre cuando una clase hija reutiliza atributos y métodos de una clase padre.

```python
class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    pass
```

- 👉 Aquí solo hay herencia (Car hereda de Vehicle).

## 🎭 Polimorfismo

El polimorfismo aparece cuando esas subclases redefinen (override) el mismo método y lo hacen comportarse distinto.

```python
class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("El auto conduce")

class Motorcycle(Vehicle):
    def move(self):
        print("La moto acelera")
```

- 👉 Mismo método (move()), distinto comportamiento → eso es polimorfismo.

## 🔑 La clave para diferenciarlos

- Herencia → reutilizar código
- Polimorfismo → mismo método, diferentes resultados

> 💡 Importante:
> La herencia no implica automáticamente polimorfismo.
> El polimorfismo aparece cuando sobrescribes métodos.

🧠 Resumen rápido

|Concepto|Qué hace|
|--|--|
|Herencia|Reutiliza código|
|Polimorfismo|Cambia comportamiento del mismo método|

## 🚫 Herencia SIN Polimorfismo

Ejemplo claro donde **hay herencia**, pero **NO hay polimorfismo**:

```python
class Vehicle:
    def move(self):
        print("El vehículo se mueve")

class Car(Vehicle):
    pass

class Motorcycle(Vehicle):
    pass

# Uso

car = Car()
motorcycle = Motorcycle()

car.move()
motorcycle.move()
```

### 🔍 ¿Qué está pasando aquí?

- Car y Motorcycle heredan de Vehicle ✅
- Pero NO redefinen el método move() ❌
- 👉 Ambos objetos ejecutan exactamente el mismo comportamiento:
  - El vehículo se mueve
  - El vehículo se mueve

🧠 ¿Por qué NO es polimorfismo?

Porque:

- No hay diferencias en el comportamiento
- No hay sobrescritura de métodos (override)
- Todos usan la misma implementación

⚖️ Comparación rápida
- ❌ Sin polimorfismo
  - Mismo método
  - Mismo comportamiento
✅ Con polimorfismo
  - Mismo método
  - Diferente comportamiento

### 💡 Idea clave

La herencia solo crea la relación entre clases.
El polimorfismo aparece cuando usas esa relación para cambiar comportamientos.

## 🎭 Polimorfismo SIN Herencia

Sí, también es posible tener **polimorfismo sin usar herencia**.  
Esto se conoce como **duck typing** en Python.

---

## 🦆 Ejemplo (Duck Typing)

```python
class Dog:
    def speak(self):
        print("Guau")

class Cat:
    def speak(self):
        print("Miau")

def make_sound(animal):
    animal.speak()

# Uso
dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)
```

###  🔍 ¿Qué está pasando?

- Dog y Cat NO heredan de una misma clase ❌
- Pero ambos tienen el método speak() ✅

👉 La función make_sound() no se preocupa por el tipo de objeto,
solo le importa que tenga un método speak().

🎯 Resultado
```bash
Guau
Miau
```

🧠 ¿Por qué esto es polimorfismo?

Porque:

- Se usa la misma función (make_sound)
- Con objetos diferentes
- Que responden de forma distinta

🦆 Regla del Duck Typing

"Si camina como pato y suena como pato, entonces es un pato"

- 👉 En Python:
  - No importa la clase
  - Importa el comportamiento

⚖️ Comparación final

|Tipo|Usa herencia|Ejemplo|
|--|--|--|
|Polimorfismo clásico|✅ Sí|Vehicle → Car|
|Duck typing (Python)|❌ No|Dog / Cat|

## 🧠 Conclusión

El polimorfismo en Python es flexible:

- Puede venir de herencia + override
- O simplemente de objetos con métodos compatibles

💡 Esto hace que Python sea muy poderoso y expresivo.