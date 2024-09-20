# 4. Dados N números, presentar por pantalla la cantidad de series crecientes de
# números cargados.

pregunta = "si"
contador = 0
number = 0
aux = 0

while pregunta=="si":
    number = int(input("ingresa un numero entero "))
    if number < aux:
        contador +=contador
    aux = number
    pregunta = input("Desea ingresar otro numero? si o no: ")

print("cantidad de series crecientes son: ", contador)