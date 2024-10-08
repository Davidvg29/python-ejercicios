# verificar si un numero ingresado entero positivo pertenece a la serie fibonacci

lista = []

aux = 0
aux1 = 1
resultado = 0

while len(lista) < 15:
    lista.append(resultado)
    aux = aux1
    aux1 = resultado
    resultado = aux + aux1

number = int(input("Ingrese un numero para verificar que pertenece a Fibonacci: "))
if number in lista:
    print("el numero SI pertenece a Fibonacci")
else:
    print("el numero NO pertenece a Fibonacci")
