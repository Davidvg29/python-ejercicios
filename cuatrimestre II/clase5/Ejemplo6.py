#   Leer el contenido del archivo ejemplo2.txt y almacenarlo en una lista

from io import open
f = open(r"C:\Users\Sistemas\Desktop\18-11\ejemplo2.txt","r")
texto = f.readlines()
f.close()
print(texto)