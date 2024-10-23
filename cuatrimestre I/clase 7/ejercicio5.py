# 5. Dado un numero natural de 4 o más dígitos, presentar por pantalla su invertido

number = int(input("Ingrese un numero para invertirlo "))
invertido = 0

while number<1000:
    number = int(input("Ingrese un numero de 4 cifras"))

while number > 0:
    ultimo = number % 10
    invertido = invertido * 10 + ultimo
    number = number//10

print("El numero invertido es ", invertido)
