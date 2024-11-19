#   Determinar si existe el archivo datos.txt

import os # sistema operativo

archivo = r"C:\Users\Sistemas\Desktop\18-11\datos.txt"

if os.path.exists(archivo):
    print("Hola existo")
else:
    print("Archivo no creado")