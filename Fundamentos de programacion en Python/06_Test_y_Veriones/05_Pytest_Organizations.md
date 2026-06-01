# Organización y estructura de pruebas en pytest: Ordenar las pruebas

## Resumen en puntos clave

### 1. ¿Por qué es importante organizar las pruebas?
- Un conjunto de pruebas desordenado dificulta la depuración y el mantenimiento.
- Las pruebas bien organizadas permiten:
  - Encontrar errores más rápidamente.
  - Comprender el propósito de cada prueba.
  - Facilitar el trabajo en equipo.
  - Reducir regresiones.
  - Refactorizar código con mayor confianza.

**Idea principal:** una buena estructura de pruebas es tan importante como las pruebas mismas.

---

# Principios clave de organización en pytest

## 2. Modularidad

La modularidad consiste en dividir las pruebas en unidades pequeñas e independientes.

### Beneficios
- Cada prueba verifica una única funcionalidad.
- Los errores son más fáciles de localizar.
- Las modificaciones afectan sólo a las pruebas relacionadas.
- Facilita la escalabilidad del proyecto.

### Ejemplo conceptual

```python
class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("No se puede dividir por cero")
        return x / y
```

### Fixture para la calculadora

```python
import pytest

@pytest.fixture
def calculator():
    return Calculator()
```

### Pruebas modulares

```python
def test_add(calculator):
    assert calculator.add(2, 3) == 5

def test_subtract(calculator):
    assert calculator.subtract(5, 2) == 3

def test_multiply(calculator):
    assert calculator.multiply(3, 4) == 12

def test_divide(calculator):
    assert calculator.divide(10, 2) == 5
```

### Ventajas

Si falla:

```python
test_divide()
```

sabemos inmediatamente que el problema está en la división y no en otra operación.

---

## 3. Convenciones de nomenclatura

Los nombres deben describir claramente qué se está verificando.

### Buenos nombres

```python
test_calculate_total_price()
test_login_successful_credentials()
test_apply_discount_correctly()
```

### Malos nombres

```python
test_1()
test_case()
test_example()
```

### Recomendaciones

#### Archivos

```text
tests/
│
├── test_products.py
├── test_users.py
├── test_orders.py
└── test_payments.py
```

#### Funciones

```python
test_user_can_login()
test_cart_adds_product()
test_discount_is_applied()
```

---

## 4. Fixtures

Los fixtures ayudan a compartir configuraciones comunes.

### Beneficios

- Evitan código duplicado.
- Mantienen consistencia.
- Facilitan mantenimiento.
- Garantizan aislamiento entre pruebas.

### Ejemplo

```python
import pytest

@pytest.fixture
def empty_cart():
    return Cart()
```

Uso:

```python
def test_add_product(empty_cart):
    empty_cart.add_product(product)

    assert len(empty_cart.products) == 1
```
___

### 5. Uso de Scope en Fixtures de pytest

En pytest, los fixtures son herramientas que permiten configurar el entorno de prueba antes de que se ejecuten las pruebas. 

Puedes definir el scope de un fixture para controlar su ciclo de vida.

Tipos de Scope en Fixtures

- function (por defecto): Crea una nueva instancia del fixture para cada función de prueba. 
  - Ideal para pruebas independientes.
import pytest

```python
@pytest.fixture(scope='function')
def mi_fixture():
    # Configuración
    resource = "Recurso"
    yield resource  # Devuelve el recurso
    # Desmontaje
    print("Desmontando recurso")

def test_1(mi_fixture):
    assert mi_fixture == "Recurso"

def test_2(mi_fixture):
    assert mi_fixture == "Recurso"
```

- class: Crea una instancia del fixture para cada clase de prueba. 
  - Util para pruebas que comparten estado entre métodos en una clase.

```python
@pytest.fixture(scope='class')
def fixture_de_clase():
    resource = "Recurso de Clase"
    yield resource
    print("Desmontando recurso de clase")

class TestClase:
    def test_1(self, fixture_de_clase):
        assert fixture_de_clase == "Recurso de Clase"

    def test_2(self, fixture_de_clase):
        assert fixture_de_clase == "Recurso de Clase"
```


- module: Crea una única instancia del fixture por módulo de prueba.    
  - Útil para configuraciones costosas que solo necesitan ser inicializadas una vez por módulo.

```python
@pytest.fixture(scope='module')
def fixture_de_modulo():
    resource = "Recurso de Módulo"
    yield resource
    print("Desmontando recurso de módulo")

def test_uno(fixture_de_modulo):
    assert fixture_de_modulo == "Recurso de Módulo"

def test_dos(fixture_de_modulo):
    assert fixture_de_modulo == "Recurso de Módulo"
```

- session: Crea una única instancia del fixture por sesión de prueba. 
  - Ideal para configuraciones que deben persistir durante toda la ejecución de las pruebas.

```python
@pytest.fixture(scope='session')
def fixture_de_sesion():
    resource = "Recurso de Sesión"
    yield resource
    print("Desmontando recurso de sesión")

def test_sesionuno(fixture_de_sesion):
    assert fixture_de_sesion == "Recurso de Sesión"
```


### Cómo Usar Fixtures con Scope en pytest

- Definir un Fixture: Usa el decorador @pytest.fixture y especifica el scope deseado.
- Inyectar el Fixture: Incluye el nombre del fixture como argumento en las funciones de prueba que lo necesiten.
- Ejecutar las Pruebas: pytest manejará automáticamente la configuración y el desmontaje según el scope especificado.

Ejemplo Completo
```python
import pytest

@pytest.fixture(scope='module')
def database_connection():
    conn = "Conexión a la base de datos"
    yield conn
    print("Cerrando conexión a la base de datos")

def test_query_1(database_connection):
    assert database_connection == "Conexión a la base de datos"

def test_query_2(database_connection):
    assert database_connection == "Conexión a la base de datos"
```

### Conclusión

El uso de scope en fixtures de pytest permite optimizar el tiempo de ejecución de las pruebas y gestionar eficazmente los recursos necesarios. Al elegir el scope adecuado, puedes mejorar la eficiencia de tus pruebas y evitar configuraciones innecesarias.


## 6. Marcadores (Markers)

Permiten clasificar pruebas.

### Ejemplo

```python
@pytest.mark.slow
def test_large_import():
    pass
```

### Marcadores personalizados

```python
@pytest.mark.payment
def test_checkout():
    pass
```

### Ejecución selectiva

```bash
pytest -m payment
```

Ejecuta únicamente las pruebas etiquetadas como `payment`.

---

## 6. Parametrización

Permite ejecutar una misma prueba con diferentes datos.

### Ejemplo

```python
import pytest

@pytest.mark.parametrize(
    "price, discount, expected",
    [
        (100, 10, 90),
        (200, 20, 180),
        (50, 5, 45)
    ]
)
def test_discount(price, discount, expected):
    assert apply_discount(price, discount) == expected
```

### Ventajas

- Menos código.
- Más cobertura.
- Pruebas más fáciles de mantener.

---

# Caso práctico: Plataforma de comercio electrónico

## Funcionalidades de productos

### Agregar productos al carrito

```python
def test_add_to_cart_successful():
    pass
```

Valida que un producto se agregue correctamente.

---

### Calcular precio total

```python
def test_calculate_total_price_accuracy():
    pass
```

Comprueba:

- Precio de productos.
- Impuestos.
- Costos de envío.
- Descuentos.

---

### Aplicación de descuentos

```python
def test_apply_discount_correctly():
    pass
```

Verifica que la promoción se aplique correctamente.

---

### Pago exitoso

```python
def test_checkout_successful_payment():
    pass
```

Valida:

- Integración con la pasarela de pago.
- Generación del pedido.
- Confirmación de compra.

---

# Caso práctico: Interacciones de usuario

## Crear cuenta

```python
def test_create_new_user_account_valid_data():
    pass
```

Comprueba que un usuario pueda registrarse.

---

## Inicio de sesión

```python
def test_login_successful_credentials():
    pass
```

Verifica autenticación correcta.

---

## Actualizar perfil

```python
def test_update_user_information_changes_saved():
    pass
```

Confirma que los cambios se guarden correctamente.

---

# Organización recomendada del proyecto

```text
project/
│
├── app/
│   ├── products.py
│   ├── users.py
│   └── payments.py
│
└── tests/
    ├── test_products.py
    ├── test_users.py
    ├── test_payments.py
    └── conftest.py
```

## ¿Qué va en `conftest.py`?

Normalmente:

```python
@pytest.fixture
def test_product():
    return Product(
        "Laptop",
        1000,
        quantity=1
    )

@pytest.fixture
def empty_cart():
    return Cart()
```

Los fixtures quedan disponibles para múltiples archivos de prueba.

---

# Buenas prácticas

✅ Una prueba = una responsabilidad.

✅ Usar nombres descriptivos.

✅ Agrupar pruebas relacionadas.

✅ Reutilizar fixtures.

✅ Utilizar parametrización para múltiples escenarios.

✅ Etiquetar pruebas mediante marcadores.

✅ Mantener independencia entre pruebas.

✅ Guardar fixtures compartidos en `conftest.py`.

---

# Errores comunes

❌ Crear un único archivo enorme con todas las pruebas.

❌ Nombres genéricos:

```python
test1()
test2()
```

❌ Repetir el mismo código de configuración.

❌ Crear dependencias entre pruebas.

❌ Mezclar pruebas de distintos módulos en un mismo archivo.

---

# Conclusión

La organización de pruebas en pytest se basa en cinco pilares fundamentales:

1. **Modularidad** → cada prueba valida una única funcionalidad.
2. **Nombres descriptivos** → facilitan la comprensión y mantenimiento.
3. **Fixtures** → reutilizan configuraciones comunes.
4. **Marcadores** → permiten clasificar y ejecutar subconjuntos de pruebas.
5. **Parametrización** → amplía la cobertura con menos código.

Un conjunto de pruebas bien estructurado no sólo detecta errores, sino que también hace que el proyecto sea más fácil de mantener, escalar y evolucionar a largo plazo.