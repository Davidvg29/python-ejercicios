#   Desarrolle una aplicacion que determine si el archivo llamado info.txt existe, en caso de existir presentar por pantalla todo su contenido, en caso de no existir crearlo y permitir que el usuario ingrese texto en el

import os
from io import open

archivo = r"C:\Users\Sistemas\Desktop\18-11\info.txt"

if os.path.exists(archivo):
    f = open(r"C:\Users\Sistemas\Desktop\18-11\info.txt","r")
    texto = f.read()
    f.close()
    print(texto)
else:
    f = open(r"C:\Users\Sistemas\Desktop\18-11\info.txt","w")
    texto = input("Hola ingresa un texto: ")
    f.write(texto)
    f.close()