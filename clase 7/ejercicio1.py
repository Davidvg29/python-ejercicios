# 1. Dado un numero entero positivo N, presentar por pantalla un mensaje que
# indique si dicho número es o no un numero primo


# number = int(input("Ingresa un numero: "))
pregunta = "si"

while pregunta=="si":
    number = int(input("Ingresa un numero: "))
    if number<2:
        print("El numero ingresado no es primo")
        pregunta=input("Desea volver a ingresar un numero? si o no: ")
    if number == 2:
        print("El numero ingresado es primo")
        pregunta=input("Desea volver a ingresar un numero? si o no: ")
    if number % 2 == 0:
        print("El numero ingresado no es primo")
        pregunta=input("Desea volver a ingresar un numero? si o no: ")
    
    factores = 1
    while factores % factores==0:
        factores=factores+1
    
    