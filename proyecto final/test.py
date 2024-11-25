listaLetras = list("abcdefghijklmnñopqrstuvwxyz")
valor = 5
mezcla = listaLetras[27-valor:] + listaLetras[:27-valor]
# mezclaInvertida = listaLetras[-(27 - valor):] + listaLetras[:-(27 - valor)]
mezclaInvertida = {mezcla[i]: listaLetras[i] for i in range(len(listaLetras))}

texto = list("buenisimo")
textoEncriptado = list("wpzidñdhk")

# encriptacion
cont=0
while len(texto) > cont:
    if texto[cont] in listaLetras:
        indice = listaLetras.index(texto[cont])
        print(f"{texto[cont]}, corresponde, {mezcla[indice]}")
    cont+=1

print("-----")

# desencriptacion
cont2=0
while len(textoEncriptado) > cont2:
    if textoEncriptado[cont2] in mezcla:
        indice = mezcla.index(textoEncriptado[cont2])
        print(f"{textoEncriptado[cont2]}, corresponde, {listaLetras[indice]}")
    cont2 += 1