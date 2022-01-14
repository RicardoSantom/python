"""1. Realiza el pseudocódigo y la codificación en lenguaje de
programación Java de un algoritmo que solicite por teclado 10
números enteros, los almacene en un vector y los muestre por
pantalla en orden inverso al de entrada."""
vector = []
for i in range(0,10):
    vector.append(int(input("Introduce un numero: ")))
for i in range(len(vector)):
    print(vector[i])
for x in range(len(vector)-1,-1,-1):
    print(vector[x])