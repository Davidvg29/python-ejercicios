# 12.Genere un programa que pida 10 valores numéricos y cree una lista con ellos a
# continuación genere dos sub listas una llamada listaA y la otra listaB, la primera
# debe tener los 5 primeros valores ingresados y la otra los siguientes 5. Presente
# en pantalla la lista original y las otras dos.

contador = 0
lista1=[]
lista2=[]

while contador<10:
    contador = contador+1
    num = int(input("ingrese un numero: "))
    if contador<=5:
        lista1.append(num)
    else:
        lista2.append(num)

print("lista 1: ", lista1)
print("lista 2: ", lista2)