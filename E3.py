""""3. Realiza el pseudocódigo y la codificación en lenguaje de
programación Java de un algoritmo que solicite por teclado las
temperaturas mínimas de cada uno de los meses del año, las
almacene en un vector y posteriormente calcule y muestre por
pantalla la temperatura media del año."""
temperaturas = []
contador = 12
for i in range(11):
   temperaturas.append(int(input("Introduzca temperatura de los meses")))
acumulador = 0
for x in range(11):
    acumulador+=temperaturas[x]
    contador+=1
print(f"La temperatura media del año es: {acumulador/contador}")