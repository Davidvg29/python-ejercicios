# 1- Dado N entero positivo determinar el mayor y el menor valor. Analice todo los casos y presente el mensaje correspondiente.

pregunta = "si"
mayor = 0
menor = 0

while pregunta=="si":
    num = int(input("ingrese un numero: "))
    if num > mayor:
        mayor = num
    if menor == 0:
        menor = num
    if menor > 0:
        if num < menor:
            menor = num
    pregunta = input("Desea seguir agregando numeros? si o no: ")

print("el numero mayor fue: ", mayor)
print("el numero menor fue: ", menor)
    