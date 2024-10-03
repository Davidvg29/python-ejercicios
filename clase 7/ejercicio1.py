# 1. Dado un numero entero positivo N, presentar por pantalla un mensaje que
# indique si dicho número es o no un numero primo

num = int(input("ingrese un numero: "))

while num<=2:
    num = int(input("ingrese un numero mayor a 2: "))
    
cont = 2
esPrimo = True
while cont<num:
    if num%cont == 0:
        esPrimo = False
        break
    cont+=1

if esPrimo:
    print("el numero es primo", num)
else:
    print("no es primo", num)