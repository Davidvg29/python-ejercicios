# dado N enteros positivos determinar la suma de los valores que son numeros primos

pregunta = "si"
sumaPrimos = 0

while pregunta == "si":
    number = int(input("Ingresa un numero entero positivo: "))
    while number <= 0 :
        number = int(input("Debes ingresar un numero entero positivo: "))
    cont = 2
    esPrimo = True
    if number != 1:
        while cont < number:
            if number % cont == 0:
                esPrimo = False
                break
            cont += 1
        if esPrimo:
            sumaPrimos = sumaPrimos + number
    pregunta = input("Desea ingresar mas numeros: si o no ")

print("la suma total de primos ingresados es: ", sumaPrimos)    