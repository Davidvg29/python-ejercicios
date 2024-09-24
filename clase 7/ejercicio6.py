# 6. Se ingresan N número enteros, presentar el promedio de los pares y el promedio
# de los impares.

pregunta = "si"

promedioImpar = 0
promedioPar = 0
contadorPar = 0
contadorImpar = 0
sumaPar = 0
sumaImpar = 0

while pregunta == "si":
    number = int(input("Ingresa un numero: "))

    if number % 2 == 0:
        contadorPar = contadorPar + 1
        sumaPar = sumaPar + number
        promedioPar = sumaPar / contadorPar
    else:
        contadorImpar = contadorImpar + 1
        sumaImpar = sumaImpar + number
        promedioImpar = sumaImpar / contadorImpar
    pregunta = input("Desea seguir agregando numeros? si o no: ")



print("El promedio de numeros pares es: ", promedioPar)
print("El promedio de numeros impares es: ", promedioImpar)
