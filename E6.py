"""6. Realiza el pseudocódigo y la codificación en lenguaje de
programación Java de un algoritmo que solicite por teclado 10
números enteros, los almacene en un vector y posteriormente
compruebe si el vector está ordenado de forma ascendente. Para
finalizar mostrará por pantalla uno de los siguientes mensajes:
“VECTOR ORDENADO” o “VECTOR NO ORDENADO”."""
vector = []
for i in range(10):
    vector.append(int(input("Introduzca entero positivo: ")))
mayor = -1
ordenado = False
j = 0
for j in range(len(vector)):
    if vector[j] >= mayor:
        mayor = vector[j]
        ordenado = True
    else:
        ordenado = False
        print("VECTOR NO ORDENADO")
        break
if ordenado:
    print("VECTOR ORDENADO")
