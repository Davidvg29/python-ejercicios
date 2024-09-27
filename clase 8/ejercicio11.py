# 11.Genere un programa que pida cinco valores numéricos y los almacene en una
# lista a continuación pida un valor N su programa debe determinar si el valor N
# está dentro de la lista y presentar por pantalla el mensaje correspondiente.

lista = []
contador = 0

while contador<5:
    contador = contador+1
    a = int(input("ingrese un valor numerico: "))
    lista.append(a)

number = int(input("ingrese un valor para buscar: "))

if number in lista:
    print("el numero si esta")
else:
    print("no existe el numero")
