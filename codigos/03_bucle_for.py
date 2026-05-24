
print("Números del 1 al 10:")

for numero in range(1, 11):
    print(numero)
print("#"*20)
print("Números pares del 10 al 0:")
for numero in range(10, -1, -2):
    print(numero)
print("#"*20)
print("Números del 0 al 20, saltando de 2 en 2:")
for numero in range(0, 21, 2):
    print(numero)
print("#"*20)

print ("letras de la palabra 'Python':")

for letra in "Python":
    print(letra)


print ("elementos de la lista [1, 2, 3, 4, 5]:")

for elemento in [1, 2, 25, 4, 5, "Hola", True, None, False, 3.14]:
    print(elemento)
