listaLetras = list("abcdefghijklmnñopqrstuvwxyz")
print(f"La lista tienen {len(listaLetras)}")
print(listaLetras)

valor = int(input("Ingrese un numero entre 0 y 27: ")) #    Ejemplo el usuario ingresa valor 5
# ¿V W X Y Z A B C D E F G H I J K L M N Ñ O P Q R S T U?

salida = listaLetras[27-valor:] + listaLetras[:27-valor]
print(salida)
texto = input("Ingresa una palabra: ")
listaTexto = list(texto)
print(listaTexto)

#index de la letra h
i = 0
indice = listaLetras.index(listaTexto[i])
print(f"La letra h corresponde {salida[indice]}")

i = 1
indice = listaLetras.index(listaTexto[i])
print(f"La letra o corresponde {salida[indice]}")

i = 2
indice = listaLetras.index(listaTexto[i])
print(f"La letra l corresponde {salida[indice]}")

i = 3
indice = listaLetras.index(listaTexto[i])
print(f"La letra a corresponde {salida[indice]}")


