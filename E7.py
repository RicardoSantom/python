"""7. Realiza el pseudocódigo y la codificación en lenguaje de
programación Java de un algoritmo que solicite por teclado 5
números enteros, los almacene en un vector y posteriormente
compruebe si el vector es capicúa, es decir, la secuencia de sus
elementos es igual vista de delante hacia atrás y de detrás
hacia adelante."""
vector = []
for i in range(5):
    vector.append(int(input("Introduzca entero positivo: ")))
capicua = True
for j in range(len(vector)):
    if vector[j] != vector[(len(vector)-1) - j]:
        capicua = False
        print("NO ES CAPICUA")
        break
    else:
        capicua = True
if capicua:
    print("ES CAPICUA")
