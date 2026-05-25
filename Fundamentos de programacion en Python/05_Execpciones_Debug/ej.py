

def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count  
    return average

def main():
    # Error intencional: lista vacía
    numbers = []
    
    # Imprimir la media
    print("Calculando la media de los números:", numbers)
    try:
        avg = calculate_average(numbers)
        print("La media es:", avg)
    except ZeroDivisionError as e:
        print("Error: No se puede calcular la media de una lista vacía.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()