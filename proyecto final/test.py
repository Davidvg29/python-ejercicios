listaMovimientos = [[1, 43501432, "11/11/2024", "14:30", "17:00", "Micro cine"]]


contadorListaMovimientos = len(listaMovimientos)
cont = 0
while cont < contadorListaMovimientos:
    cont2 = 0
    while cont2 < len(listaMovimientos[cont]):
        print(listaMovimientos[cont][cont2])
        cont2+=1
    cont+=1