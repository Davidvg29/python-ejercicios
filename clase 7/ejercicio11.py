# 11.Se ingresan N valores numéricos. Determinar la posición y el valor del mayor
# numero par y el menor impar de los valores ingresados. Presentar por pantalla los
# resultados.

pregunta = "si"
mayorPar = 0
menorImpar = 0

while pregunta == "si":
    number = int(input("ingrese un numero: "))
    if number % 2 == 0 and number>mayorPar:
        mayorPar = number
    if menorImpar == 0:
        menorImpar = number
    if menorImpar>0:
        if number % 2 !=0 and number<menorImpar:
            menorImpar= number
    pregunta=input("desea un numero mas? si o no: ")

print("mayor par: ", mayorPar)
print("menor Impar: ", menorImpar)