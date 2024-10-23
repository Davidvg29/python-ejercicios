# 7. Se ingresan N valores numéricos. Se dese saber cuántos son positivos, cuantos
# negativos y cuantos iguales a cero.

positivos = 0
negativos = 0
cero = 0

pregunta = "si"

while pregunta=="si":
    number = int(input("Ingresa un numero: "))
    if number>0:
        positivos = positivos +1
    elif number<0:
        negativos = negativos + 1
    else:
        cero = cero+1
    pregunta = input("Desea ingresar mas numeros? si o no: ")

print("ingresaste los siguientes numeros:")
print("Positivos: ", positivos)
print("Negativos: ", negativos)
print("Igual a cero: ", cero)