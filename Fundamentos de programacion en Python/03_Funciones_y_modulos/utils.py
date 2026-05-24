NOMBRE= "MI UTILS"

CONSTANTE_EJEMPLO = 3.14

def pasar_a_mayusculas(texto):
    return texto.upper()

def pasar_a_minusculas(texto):
    return texto.lower()

def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hablar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")


if __name__ == "__main__":
    print(NOMBRE)
    print(CONSTANTE_EJEMPLO)

    texto = "Hola Mundo"
    print(pasar_a_mayusculas(texto))
    print(pasar_a_minusculas(texto))
    print(contar_palabras(texto))

    e = Persona("Juan", 30)
    e.hablar()
