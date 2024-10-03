# 8- Dado N entero positivo determina todos los números tales que sean iguales a la suma de sus divisores

num = int(input("ingrese un numero positivo: "))
while num<1:
    num = int(input("ingrese un numero positivo: "))

cont = 0
suma = 0
while cont < num:
    cont+=1
    if num%cont == 0:
        suma = suma + cont

print("suma de divisores de ", num, " es ", suma)