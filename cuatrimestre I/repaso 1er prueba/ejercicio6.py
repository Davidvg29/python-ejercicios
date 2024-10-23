# 6- Dado N entero positivo encuentre el primo más cercano a él y superior a N

num = int(input("ingrese un numero entero positivo: "))

while num<=1:
    num = int(input("ingrese un numero entero positivo mayor a 1: "))

primoEncontrado = num + 1 
while True:
    esPrimo = True  
    cont = 2  

    while cont < primoEncontrado: 
        if primoEncontrado % cont == 0: 
            esPrimo = False 
            break  
        cont += 1  

    if esPrimo: 
        break  

    primoEncontrado += 1  

print("El primo mas cercano y mayor a", num, "es: ", primoEncontrado)