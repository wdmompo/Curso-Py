# Explorando las Pruebas en Python con pytest

En esta sesión, aprenderás sobre **pytest**, un marco de pruebas en Python. Veremos cómo instalar pytest, escribir funciones de prueba y ejecutar pruebas desde la línea de comandos.

## ¿Qué es pytest?

**pytest** es un marco de pruebas que facilita la escritura de pruebas pequeñas y legibles, así como su escalabilidad para pruebas funcionales complejas. Es como una red de seguridad para tu código, ayudando a detectar errores en etapas tempranas del desarrollo, lo que ahorra tiempo y evita dolores de cabeza en el futuro.

## Importancia de las Pruebas

Construir software sin pruebas es como construir una casa sin verificar los cimientos. Sin pruebas, estás operando sobre un terreno inestable. La sintaxis de pytest es limpia e intuitiva, lo que facilita la escritura y comprensión de las pruebas.

## Instalación y Ejemplo Básico

Instalar pytest es sencillo. Ejecuta el siguiente comando en tu terminal:

```bash
pip install pytest
```

Crear Archivos

calculator.py: Archivo básico con una función sencilla.
test_calculator.py: Archivo de prueba donde pytest descubre automáticamente las funciones de prueba.

Ejemplo de Prueba

```python
# calculator.py
def add(a, b):
    return a + b

# test_calculator.py
def test_add():
    assert add(2, 3) == 5
```

Ejecuta la prueba desde la línea de comandos:

```bash
pytest
```

Si introduces un error en la función y vuelves a ejecutar la prueba, pytest detectará el error y te indicará dónde está el problema.

## Parametrización de Pruebas

La función de parametrización permite probar la función de adición con múltiples conjuntos de entradas y salidas esperadas:

```python
import pytest

@pytest.mark.parametrize("input1, input2, expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0)
])
def test_add(input1, input2, expected):
    assert add(input1, input2) == expected
```

## Accesorios en pytest

Los accesorios son funciones que proporcionan una base para realizar pruebas confiables. Se utilizan para establecer condiciones previas para pruebas, como inicializar bases de datos o crear datos de prueba. Se definen con el decorador @pytest.fixture.
Ejemplo de Accesorio

```python
import pytest

@pytest.fixture
def sample_data():
    return [1, 2, 3]

def test_sum(sample_data):
    assert sum(sample_data) == 6
```

## Dispositivos Mejorados

Los dispositivos pueden realizar cálculos o transformaciones en los datos. Aquí hay un ejemplo de un dispositivo que crea una lista de números y los duplica:

```python
@pytest.fixture
def enhanced_data():
    data = [1, 2, 3]
    return [x * 2 for x in data]

def test_sum_enhanced(enhanced_data):
    assert sum(enhanced_data) == 12
```

## Conclusión

Las pruebas son un proceso continuo. Desarrolla tu código y sigue escribiendo pruebas para garantizar la corrección y estabilidad. Con pytest, estarás bien equipado para crear aplicaciones Python sólidas. ¡Eso es todo por esta sesión!

___

# Técnicas Avanzadas en pytest

En este vídeo, ampliaremos tus conocimientos sobre **pytest** y cubriremos técnicas avanzadas que simplificarán tus pruebas y te ayudarán a detectar más errores. Al final, podrás:

- Implementar técnicas de **parametrización** en pytest.
- Examinar escenarios de prueba complejos.
- Utilizar dispositivos y técnicas de organización para lograr una cobertura de prueba eficiente.

## ¿Por qué son importantes las técnicas avanzadas?

A medida que los proyectos se vuelven complejos, las funciones avanzadas de pytest ofrecen herramientas especializadas para realizar pruebas adaptables y mejorar la cobertura. Esto incluye:

- **Datos de prueba reutilizables**.
- **Rutinas de configuración** que reducen la redundancia y mejoran la mantenibilidad.

## Ejecución de Pruebas con Diferentes Entradas

Ejecutar la misma función de prueba con diferentes valores garantiza que el código maneje varios escenarios de manera eficiente. La estructuración lógica de las pruebas mejora la navegación, comprensión y mantenimiento a medida que el proyecto escala.

### Dispositivos en pytest

Los dispositivos son funciones que se ejecutan antes o después de las funciones de prueba, garantizando un entorno controlado. 

- **Cree datos de prueba complejos** una vez y compártalos en varias pruebas.
- Configure condiciones previas específicas, como conexiones a bases de datos o respuestas de API simuladas.

## Parametrización

La **parametrización** en pytest permite probar tu código con numerosos valores de entrada, garantizando que maneje diversas situaciones delicadamente.

- Permite probar sistemáticamente **valores límite**, **entradas no válidas** y **casos extremos**, descubriendo problemas ocultos.

### Ejemplo de Parametrización

Imagina un formulario de registro que valida información de usuario. La parametrización te permite probar exhaustivamente el código con varias entradas, aumentando la confianza en la gestión de diversos escenarios.

## Organización de Pruebas

Mantener un conjunto de pruebas bien organizado es crucial para el mantenimiento y la navegación eficiente. 

- **Estructura lógica**: Organiza las pruebas en módulos, clases o directorios que reflejen la base de código.
- Utiliza **marcadores** como `@pytest.mark.skip` o `@pytest.mark.xfail` para categorizar y controlar la ejecución de pruebas.

### Beneficios de una Buena Organización

Un conjunto de pruebas bien organizado es como una biblioteca bien mantenida. Mejora la legibilidad del código y simplifica la incorporación de nuevos miembros al equipo.

## Consejos y Atajos Profesionales

- **Nombres claros**: Elige nombres informativos para tus funciones de prueba.
- **Evita dependencias**: Asegúrate de que las pruebas se puedan ejecutar en cualquier orden.

## Conclusión

Dominar las funciones avanzadas de pytest es crucial para los desarrolladores de Python que desean crear software sólido y confiable. Al final de este vídeo, estarás listo para implementar técnicas avanzadas en pytest y enfrentar con confianza situaciones del mundo real.

Está desarrollando una función de biblioteca de Python que realiza cálculos complejos basados en varios parámetros de entrada. Quiere asegurarse de que esta función maneja correctamente múltiples escenarios de entrada y casos extremos. ¿Qué función avanzada de pytest es la más adecuada para lograr este objetivo? Seleccione la mejor respuesta.

- Accesorios
- Organización de pruebas
- Afirmaciones
- **Parametrización**

Correcto
> Correcto La parametrización le permite ejecutar la misma función de prueba con diferentes valores de entrada, probando eficientemente varios escenarios y casos extremos sin escribir funciones de prueba separadas.