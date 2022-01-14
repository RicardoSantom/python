"""2. Realiza el pseudocódigo y la codificación en lenguaje de
programación Java de un algoritmo que solicite por teclado 10
números enteros, los almacene en un vector y posteriormente
muestre por pantalla cuantos de dichos números son impares.
"""
vector = []
for i in range(0,10):
    vector.append(int(input("Introduce un numero: ")))
    contador = 0
for x in range(0,10):
    par = vector[x]%2
    if par!= 0:
        contador+=1
print(f"Hay {contador} numeros impares.")