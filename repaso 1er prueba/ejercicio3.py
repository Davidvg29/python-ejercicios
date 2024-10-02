# 3. Ingrese numero mientas sean distintos de cero a continuación ordenar los números impares de mayor a menor sin tener los pares presentes la lista de los valores ingresados y la lista ordenada.

pregunta = "si"
array = []
while pregunta == "si":
    num = int(input("Ingrese un numero: "))
    while num == 0:
        num = int(input("Ingrese un numero distinto a cero: "))
    if num%2 == 0:
        array.append(num)
    pregunta=input("desea ingresar mas numeros?")

array.sort()
array.reverse()
print(array)