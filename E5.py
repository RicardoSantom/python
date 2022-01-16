"""5. Realiza el pseudocódigo y la codificación en lenguaje de
programación Java de un algoritmo que solicite por teclado 10
números enteros, los almacene en un vector y muestre por
pantalla el mayor y la posición que ocupa."""
vector = []
for i in range(10):
    vector.append(int(input("Introduzca entero positivo: ")))
mayor = 0
pos = -1
for j in range(10):
    if vector[j] > mayor:
        mayor = vector[j]
        pos = j
print(f"El numero mayor es el ", mayor, " y se ha encontrado en la posicion ", pos + 1)
