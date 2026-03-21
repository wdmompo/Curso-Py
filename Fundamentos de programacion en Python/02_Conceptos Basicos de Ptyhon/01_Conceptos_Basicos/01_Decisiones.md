# 🧠 Sentencias de Decisión y Selección en Programación

En el mundo de la programación, donde el código interactúa con entornos cambiantes y diversas entradas, es fundamental tomar decisiones informadas. Las **sentencias de decisión y selección** constituyen la base de la lógica programática, permitiendo al código evaluar información y elegir acciones, de manera similar al pensamiento humano.

---

## 🔹 Sentencias de decisión: Control del flujo

Toda decisión se basa en una pregunta clave: **¿la condición es verdadera o falsa?**

Las sentencias de decisión evalúan condiciones (simples o complejas) y determinan el flujo del programa.

### Ejemplo básico (`if`):

```python
if order_total >= 50:
  print("Congratulations! You qualify for free shipping.")
```

- Si order_total >= 50 → se ejecuta el mensaje.
- Si no → no ocurre nada.

## 🔹 Sentencias de selección: Más opciones

Las estructuras como if-elif-else permiten evaluar múltiples condiciones.

- Ejemplo con else:

```python
if order_total >= 50:
  print("Congratulations! You qualify for free shipping.")
else:
  print("Add more items to your cart to reach the free shipping threshold!")
```

- 🔹 Uso de elif (múltiples condiciones)

Permite manejar más de dos posibilidades. Python evalúa de arriba hacia abajo y ejecuta solo la primera condición verdadera.

```python
if points >= 1000:
  print("You've achieved Platinum status! Enjoy exclusive benefits.")
elif points >= 500:
  print("You're a Gold member! Thank you for your loyalty.")
elif points >= 100:
  print("Welcome to the Silver tier! Start earning rewards.")
else:
  print("You're a Bronze member. Keep shopping to earn more points!")
```

## 🔹 Condiciones anidadas y lógica booleana

### 📌 Condiciones anidadas

Permiten crear estructuras jerárquicas de decisión (if dentro de if).

### 📌 Lógica booleana

#### Uso de operadores:

- and (y)
- or (o)
- not (no)

Ejemplo:

```python
if age >= 65 and is_student:
```

⚠️ Es importante definir previamente las variables booleanas:

```python
is_student = True
```

🌍 Aplicaciones reales

Estas estructuras son fundamentales en múltiples sistemas:

- 🚗 Vehículos autónomos: toman decisiones en tiempo real.
- 💳 Detección de fraude: identifican transacciones sospechosas.
- 🎓 Aprendizaje personalizado: adaptan contenido al estudiante.
- 🏠 Domótica: automatizan tareas del hogar.
- 🎮 Videojuegos: crean comportamientos dinámicos en personajes.
- ⚠️ Complejidad y mantenimiento

### El uso excesivo de estructuras if-else puede generar código:

- Difícil de leer
- Complejo de mantener
- Propenso a errores

## ✅ Buenas prácticas:

- Modularizar en funciones
- Usar nombres descriptivos
- Escribir comentarios claros

## 🚀 Optimización de decisiones
### 📌 Uso de diccionarios

Alternativa más limpia cuando hay muchas opciones:

```python
shipping_rates = {
  "US": 5,
  "EU": 10,
  "AR": 7
  }
```

### 📌 Uso de bibliotecas

Herramientas como:

- NumPy
- Pandas

Permiten operaciones condicionales más eficientes en grandes volúmenes de datos.

## ✅ Conclusión

- Las sentencias de decisión y selección:
- Permiten que el código analice, decida y actúe
- Son esenciales para programas dinámicos
- Bien utilizadas, producen código claro, eficiente y mantenible

👉 Dominar estos conceptos es clave para desarrollar software de calidad.

## Pregunta

### Usted está desarrollando un programa Python para automatizar el proceso de clasificación de tickets de soporte al cliente basado en su nivel de urgencia. ¿Cuál de los siguientes escenarios demuestra MEJOR el uso de sentencias condicionales en este contexto? Elija la mejor respuesta.


- [ ] Mostrar un mensaje de bienvenida al agente de atención al cliente cuando se conecta al sistema.
- [ ] Cálculo del tiempo medio de respuesta para todas las solicitudes de asistencia, independientemente de su urgencia.
- [ ] Almacenamiento de todos los tickets de atención al cliente en una lista, independientemente de su urgencia o contenido.
- [x] Asignación de tickets etiquetados como "urgentes" a una cola prioritaria y notificación inmediata a los miembros del equipo correspondientes.

> Correcto Se trata de utilizar sentencias condicionales para evaluar el nivel de urgencia de cada ticket y desencadenar acciones específicas en función de esa condición.

