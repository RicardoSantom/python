"""4. Realiza el pseudocódigo y la codificación en lenguaje de
programación Java de un algoritmo que solicite por teclado 5
nombres de usuario y los almacene en un vector. A continuación
solicitará un nombre de usuario y deberá buscarlo en el vector.
Para finalizar mostrará por pantalla si lo ha encontrado o no.
En caso afirmativo también deberá mostrar la posición."""
vector = []
for i in range(5):
    vector.append(str(input("Introduzca nombres para usuarios(5): ")))
nombre = str (input("Introduzca nombre a buscar"))
pos = -1
for x in range(len(vector)):
    if nombre == vector[x]:
        pos = x
if pos != -1:
    print(f"Nombre encontrado en la posicion {pos+1}")
else:
    print("Nombre no encontrado.")