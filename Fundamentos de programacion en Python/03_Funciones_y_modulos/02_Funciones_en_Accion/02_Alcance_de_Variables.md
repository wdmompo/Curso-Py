## 📘 Alcance de variables en Python

### 🧩 Concepto clave
- El **alcance (scope)** determina:
  - **Dónde** se puede acceder a una variable.
  - **Cuánto tiempo** existe en el programa.

---

## 🔑 Tipos principales de alcance

### 📍 Alcance local
- Las variables se crean dentro de una función.
- **Solo se pueden usar dentro de esa función**.
- Cuando la función termina, las variables:
  - Dejan de existir
  - No pueden ser accedidas desde fuera

🧠 Idea clave:
- Son temporales y están aisladas.

✅ Ventajas del ámbito local

- Encapsulación: mantiene datos dentro de su contexto
- Evita colisiones de nombres
- Uso eficiente de memoria (se crean y destruyen automáticamente)

---

### 🌍 Alcance global
- Las variables se definen fuera de cualquier función.
- **Se pueden acceder desde cualquier parte del código**.

🧠 Idea clave:
- Son compartidas y persistentes durante la ejecución del programa.

```python
COMPANY_NAME = "Global Tech Solutions"

def print_welcome_message():
    print("Welcome to", COMPANY_NAME.upper())

def print_contact_info():
    print("Contact", COMPANY_NAME, "at info@globaltechsolutions.com")

print_welcome_message()
print_contact_info()
```

⚠️ Problemas del uso excesivo

- Código más difícil de entender
- Efectos secundarios inesperados
- Más difícil de depurar y testear
- Riesgo de conflictos de nombres

---

### ⚖️ Diferencias principales

| Tipo de alcance | Acceso | Duración |
|-----------------|--------|----------|
| Local           | Solo dentro de la función | Mientras la función se ejecuta |
| Global          | En todo el programa       | Durante toda la ejecución |


### 🧩 Ámbitos anidados (Enclosing)

- Funciones dentro de funciones.
- La función interna puede acceder a variables de la externa.

🧪 Ejemplo:

```python
def outer_function():
    outer_var = "Hello from the outer function!"
    
    def inner_function():
        print(outer_var)
    
    inner_function()

outer_function()
```

## 📏 Regla LEGB (orden de búsqueda)

Cuando Python busca una variable sigue este orden:

1. L (Local) → dentro de la función actual
2. E (Enclosing) → funciones externas (anidadas)
3. G (Global) → nivel del módulo
4. B (Built-in) → funciones internas de Python (print, list, etc.)

## ⚠️ Modificación de variables globales

Se puede usar `global`, pero no es recomendable.
Puede generar errores difíciles de detectar.

✔️ Mejor opción:

- Pasar variables como argumentos
- Devolver valores con return


---

## ⚠️ Buenas prácticas

### ✔️ Ventajas del alcance local
- Mantiene el código **organizado**
- Evita **cambios accidentales**
- Reduce errores

### ⚠️ Riesgos del alcance global
- Puede causar **efectos secundarios inesperados**
- Cambios en una parte del código afectan otras
- Hace el código más difícil de depurar

---

## 🧠 Analogía útil

- **Variables locales** → como archivos dentro de una carpeta específica (solo se usan ahí)
- **Variables globales** → como configuraciones compartidas por todo el sistema

---

## 🎯 Conclusión

- Entender el alcance es clave para:
  - Escribir código limpio
  - Evitar errores
  - Mejorar la organización

- Usar variables locales siempre que sea posible y **ser cuidadoso con las globales**.