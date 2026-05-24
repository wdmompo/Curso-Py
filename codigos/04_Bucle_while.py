
salir = False

while not salir:
    numero = input("Introduce un número o \"salir\" \n :")
    
    if numero == "salir":
        salir = True
        print("¡Hasta luego!")
    else:
        print(f"Has introducido el número: {numero}")
