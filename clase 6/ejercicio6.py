# 6. Dado un numero natural N, presentar en forma decreciente los N primeros
# números

numero = int(input("Ingrese un numero: "))
contador = numero

while contador>0:
    print("El siguiente numero decreciente es: ", contador)
    contador= contador-1
    