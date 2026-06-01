# Progreso en Pruebas Unitarias

A medida que progresas de ser un programador de Python de nivel básico a un desarrollador más experimentado, una práctica crucial que impacta la calidad y fiabilidad de tu código son las **pruebas unitarias**. Piensa en ellas como un mecánico que inspecciona cada pieza de un motor antes de montarlo. Asegurarse de que cada componente funcione correctamente minimiza las averías inesperadas en el sistema.

## ¿Qué son realmente las pruebas unitarias?

Las pruebas unitarias son una forma sistemática de diseccionar el código en sus componentes más fundamentales, llamados "unidades". En Python, estas unidades son típicamente funciones o clases. Cada unidad debe ser relativamente autónoma y centrada.

### Creación de Casos de Prueba

Una vez identificadas las unidades, creamos "Casos de prueba", que son programas en miniatura para evaluar cada unidad. Estos casos introducen diferentes datos, observan las reacciones y comprueban que los resultados se ajusten a nuestras expectativas, simulando diversos escenarios.

## Importancia de las Pruebas Unitarias

La belleza de las pruebas unitarias radica en su capacidad para detectar problemas en fases tempranas del desarrollo. Un pequeño error en una función puede provocar fallos significativos en toda la aplicación. Probar rigurosamente cada unidad permite identificar y solucionar problemas antes de que causen daños.

### Terminología Clave

- **Aserciones**: Verifican si tu código se comporta como se espera. Por ejemplo, si una función `add_numbers(2, 3)` debería devolver 5.
  
- **Casos de prueba**: Un conjunto de aserciones que someten a una unidad de código a un entrenamiento exhaustivo, garantizando que maneja correctamente diversas entradas.

- **Conjunto de pruebas**: Una colección de rutinas que abarca múltiples casos de prueba, asegurando que cada parte del código funcione correctamente.

- **Ejecutor de pruebas**: Una herramienta que ejecuta todos los casos de prueba y reporta los resultados.

## Por qué son importantes las pruebas unitarias

Las pruebas unitarias son indispensables porque:

- **Detección de errores**: Actúan como pequeños detectives que examinan el código para evitar que los errores pequeños se multipliquen.
  
- **Confianza en el código**: Permiten realizar cambios y refactorizaciones sin miedo a romper algo más, proporcionando una red de seguridad.

- **Mejora del diseño**: Fomentan un diseño modular y un código más fácilmente mantenible.

- **Documentación viva**: Actúan como documentación que muestra cómo debe utilizarse el código.

## El Ciclo de Pruebas Unitarias

Las pruebas unitarias son un proceso cíclico que se integra en el flujo de trabajo de desarrollo:

1. **Escribir código**: Crear funciones, clases o módulos.
  
2. **Escribir pruebas**: Definir expectativas de comportamiento para el código.
  
3. **Ejecutar las pruebas**: Verificar si los resultados coinciden con las expectativas.

4. **Corregir y repetir**: Investigar y ajustar el código si una prueba falla, continuando el ciclo.

## Escenario Real: Ejemplo Sencillo

Supongamos que estás creando una aplicación de calculadora en Python. Tienes una función llamada `calculate_discount(price, percentage)` que calcula el precio con descuento. Aquí tienes una prueba unitaria para esta función utilizando el módulo `pytest`:

```python
import pytest

def calculate_discount(price, percentage):
    return price - (price * percentage / 100)

class TestDiscountCalculation:
    def test_ten_percent_discount(self):
        result = calculate_discount(100, 10)
        assert result == 90  # Aserción

    def test_invalid_input(self):
        # Aquí podrías agregar casos de prueba para entradas inválidas
```

## Conclusión

Las pruebas unitarias son una habilidad fundamental que te permite crear aplicaciones Python más robustas y fiables. Al descomponer tu código y probar cada unidad, ganarás confianza para refactorizar y expandir tus proyectos sin miedo. ¡Abraza el ciclo de pruebas unitarias y recuerda que cada prueba exitosa es una victoria en tu camino para convertirte en un desarrollador competente!


## ¿Cuál es el objetivo principal de las pruebas unitarias en el desarrollo de software? Seleccione la mejor respuesta.

- Para verificar que el software cumple los requisitos del usuario 
- **Identificar y corregir errores en una fase temprana del ciclo de desarrollo**
- Integrar diferentes módulos del software 
- Para garantizar el rendimiento del software bajo cargas pesadas 

Buen trabajo
> Correcto Las pruebas unitarias ayudan a detectar y resolver errores en una fase temprana, lo que garantiza una base de código más estable. 

## ¿Cuál de las siguientes afirmaciones es cierta sobre las aserciones en las pruebas unitarias? Seleccione todas las que correspondan. 

- **Las aserciones ayudan a verificar que el código se comporta como se espera**

Buen trabajo
> Correcto Las aserciones se utilizan para garantizar que el código produce los resultados esperados. 

- Las aserciones pueden corregir automáticamente errores en el código 
- **Las aserciones son un componente clave de la redacción de casos de prueba**

Buen trabajo
> Correcto Las aserciones son esenciales en los casos de prueba para validar el comportamiento del código. 

- Las aserciones pueden sustituir a las pruebas de integración 

## Usted está escribiendo una prueba unitaria para una función llamada calculate_discount(price, is_member). ¿Cuál de los siguientes sería el enfoque más apropiado para esta prueba unitaria? Seleccione la mejor respuesta.  


- **Para comprobar que la función devuelve el importe de descuento correcto para diferentes valores de entrada de price y is_member.**
- Para verificar que el software cumple los requisitos del usuario
- Integrar diferentes módulos del software
- Para garantizar el rendimiento del software bajo cargas pesadas

Buen trabajo
> Correcto Esto prueba correctamente la funcionalidad de la función.

## Un desarrollador es nuevo en el mundo de las pruebas y le pregunta sobre la práctica de las pruebas unitarias. ¿Cuál sería la mejor manera de describirle las pruebas unitarias? Seleccione la mejor respuesta.

- Las pruebas unitarias son un método para probar toda la aplicación a la vez y asegurarse de que todo funciona correctamente.
- **Las pruebas unitarias consisten en probar componentes o funciones individuales del código de forma aislada para verificar su correcto comportamiento.**
- Las pruebas unitarias son lo mismo que las pruebas de aceptación del usuario, en las que los usuarios finales prueban la aplicación.
- Las pruebas unitarias sólo se realizan al final del proceso de desarrollo para garantizar que todo funciona según lo esperado.

Buen trabajo
> Correcto Las pruebas unitarias se centran en probar unidades individuales de código.

## Está explicando las pruebas unitarias a una parte interesada no técnica. ¿Cuál de estas descripciones es la más adecuada? Seleccione la mejor respuesta.

- **Las pruebas unitarias son como comprobar las piezas individuales del motor de un coche antes de montarlo entero.**
- Las pruebas unitarias son el último paso antes de poner el software a disposición de los usuarios.
- Las pruebas unitarias las realizan los usuarios finales para asegurarse de que el software satisface sus necesidades.
- Las pruebas unitarias sólo son necesarias en proyectos de software grandes y complejos.

Buen trabajo
> Correcto. Es una buena analogía Destaca la idea de probar los componentes individuales antes de integrarlos.
