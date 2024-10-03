# 3. Ingrese numero mientas sean distintos de cero a continuación ordenar los números impares de mayor a menor sin tener los pares presentes la lista de los valores ingresados y la lista ordenada.

pregunta = "si"
array = []
impares = []
while pregunta == "si":
    num = int(input("Ingrese un numero: "))
    while num == 0:
        num = int(input("Ingrese un numero distinto a cero: "))
    array.append(num)
    if num%2 != 0:
        impares.append(num)
    pregunta=input("desea ingresar mas numeros?")

impares.sort()
impares.reverse()
print(array)
print(impares)