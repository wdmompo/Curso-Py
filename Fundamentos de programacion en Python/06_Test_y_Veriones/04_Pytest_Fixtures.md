# Pytest Fixtures: Prepara el escenario para tus pruebas

Resumen en puntos clave

## 1. ¿Qué es pytest?

pytest es uno de los frameworks de pruebas más populares para Python.
Permite crear y ejecutar pruebas de forma sencilla y flexible.
Está diseñado para minimizar el código repetitivo y facilitar la lectura de las pruebas.
Ayuda a detectar errores antes de que lleguen a producción.

## 2. ¿Por qué usar pytest?

Sintaxis simple e intuitiva.
Fácil integración con proyectos Python.
Reduce la complejidad de configuración.
Posee un amplio ecosistema de plugins.
Facilita la automatización de pruebas y mejora la calidad del software.

## 3. Funciones de prueba (Test Functions)
Son funciones Python cuyo nombre comienza con test_.
Contienen assertions (assert) para verificar comportamientos esperados.
Si una aserción falla, pytest informa el error.

Ejemplo:
```python
def test_suma():
    assert 2 + 2 == 4
```

## 4. Fixtures

Los fixtures son uno de los elementos más poderosos de pytest.

### ¿Para qué sirven?

- Preparar recursos antes de una prueba.
- Liberar recursos al finalizar.
- Reutilizar configuraciones comunes.
- Mantener las pruebas aisladas entre sí.

Ejemplos de uso:

- Conexiones a bases de datos.
- Clientes HTTP.
- Datos de prueba.
- Objetos simulados (mocks).

## 5. Parametrización

Permite ejecutar la misma prueba con múltiples conjuntos de datos.

### Ventajas:

- Menos código duplicado.
- Mayor cobertura de pruebas.
- Fácil validación de distintos escenarios.

Ejemplo conceptual:

```python
@pytest.mark.parametrize(
    "entrada, salida",
    [
        (1, 2),
        (2, 4),
        (3, 6)
    ]
)
def test_doble(entrada, salida):
    assert entrada * 2 == salida
```

## 6. Marcadores (Markers)

Permiten etiquetar pruebas.

Usos comunes:

- Ejecutar sólo pruebas lentas.
- Omitir pruebas específicas.
- Clasificar pruebas por categorías.

Ejemplo:

```python
@pytest.mark.database
def test_guardar_usuario():
    pass
```

## 7. Plugins

Una de las mayores fortalezas de pytest.

Existen plugins para:

- Aplicaciones web.
- Bases de datos.
- Código asíncrono.
- Cobertura de código.
- Generación de reportes.
- Integración continua (CI/CD).

## Caso práctico 1: Aplicaciones Web con Flask

Objetivo

Comprobar que una aplicación web funciona correctamente.

Qué permite probar pytest

- Rutas HTTP.
- Formularios.
- Inicio de sesión.
- APIs REST.
- Operaciones sobre la base de datos.
- Fixture para un cliente Flask

```python
import pytest
from your_flask_app import app

@pytest.fixture
def client():
    """
    Crea un cliente de pruebas para la aplicación Flask.
    """
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client
```

Explicación

```python
@pytest.fixture
```

Define un fixture reutilizable.

```python
app.config['TESTING'] = True
```

Activa el modo de pruebas.

```python
with app.test_client() as client:
```

Crea un cliente HTTP simulado.

```python
yield client
```

Entrega el cliente a las pruebas y luego libera recursos.

## Caso práctico 2: Ciencia de Datos

Objetivo

Garantizar que:

- Los datos se limpian correctamente.
- Los modelos producen resultados válidos.
- Las métricas son las esperadas.
- Fixture con datos de prueba

```python
import pytest
import pandas as pd

from your_data_science_project import (
    clean_data,
    train_model,
    predict
)

@pytest.fixture
def test_data():
    data = {
        'feature1': [1, 2, 3, None],
        'feature2': ['A', 'B', 'C', 'D']
    }

    return pd.DataFrame(data)
```

Explicación
```python
@pytest.fixture
```
Crea datos reutilizables para múltiples pruebas.
```ppython
data = {...}
```

Define datos de ejemplo.
```python
pd.DataFrame(data)
```

Convierte los datos en un DataFrame de Pandas.

## pytest vs unittest

| Característica       | pytest | unittest  |
| -------------------- | ------ | --------- |
| Sintaxis simple      | ✅    | ❌       |
| Fixtures             | ✅    | Limitado  |
| Parametrización      | ✅    | ❌       |
| Plugins              | ✅    | Muy pocos |
| Menos código         | ✅    | ❌       |
| Curva de aprendizaje | Baja   | Media     |


Conclusión: aunque unittest forma parte de la biblioteca estándar de Python, muchos desarrolladores prefieren pytest por su simplicidad y potencia.

Reto de codificación

Objetivo

Verificar que la función contains_five() detecta correctamente el número 
5 dentro de una lista.


Solución

```python
def test_contains_five():
    """
    Comprueba que contains_five detecta el número 5.
    """

    my_list = [1, 3, 5, 7, 9]

    assert contains_five(my_list) is True
```

Explicación
```python
my_list = [1, 3, 5, 7, 9]
```
Lista de prueba que contiene el número 5.
```python
contains_five(my_list)
```
Ejecuta la función a validar.
```python
assert contains_five(my_list) is True
```
La prueba pasa únicamente si la función devuelve True.

Buenas prácticas para probar contains_five()

Además de la prueba anterior, conviene verificar:

- No contiene 5
[1, 2, 3, 4]

- Lista vacía
[]

- Solo contiene 5
[5]

- Múltiples apariciones
[5, 5, 5]

Esto mejora la cobertura y ayuda a detectar errores ocultos.

## Conclusión

pytest es un framework moderno, simple y potente para pruebas en Python.
Los fixtures permiten preparar y reutilizar entornos de prueba.
La parametrización facilita probar múltiples escenarios.
Los marcadores ayudan a organizar pruebas.

Los plugins amplían enormemente las capacidades de pytest.
Es especialmente útil en proyectos web, ciencia de datos, APIs y aplicaciones empresariales.

Una buena suite de pruebas aumenta la confiabilidad, mantenibilidad y calidad del código.