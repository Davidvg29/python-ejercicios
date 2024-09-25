# 10.Se ingresan N valores numéricos. Determinar el mayor y el menor de los valores
# ingresados.

pregunta ="si"
mayor=0
menor=0

while pregunta=="si":
    number=int(input("ingrese un numero: "))
    if number>mayor:
        mayor = number
    if menor==0:
        menor = number
    if menor>0:
        if number<menor:
            menor=number
    pregunta=input("desea ingresar un numero mas? si o no: ")

print("el numero mayor ingresado es: ", mayor)
print("el numero menor ingresado es: ", menor)