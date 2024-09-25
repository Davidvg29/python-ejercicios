# 8. Se ingresan N valores numéricos y un valor particular X, determinar cuántas
# veces está presente el valor X entre los N números ingresados.

x = int(input("Ingresa el valor particular X: "))
pregunta = "si"
contador = 0

while pregunta=="si":
    number = int(input("Ingresa un numero: "))
    if number == x:
        contador= contador+1
    pregunta= input("Desea agregar mas numeros? si o no: ")

print("el valor particular X se ingreso ", contador, " veces")