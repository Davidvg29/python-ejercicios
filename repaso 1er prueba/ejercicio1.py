#dado n numeros enteros positivos determinar el mayor y el menor valor analize todos los casos y muestre el mensaje

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
    