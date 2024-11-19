#   Leer el contenido del archivo ejemplo2.txt

from io import open
f = open(r"C:\Users\Sistemas\Desktop\18-11\ejemplo2.txt","r")   # aqui va el nombre y r
texto = f.read()
f.close()
print(texto)