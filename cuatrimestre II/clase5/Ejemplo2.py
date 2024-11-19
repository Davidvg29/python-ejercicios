#   Crear un archivo llamado ejemplo2.txt y agragar las siguientes lineas
#   Linea1
#   Linea2
#   Linea3

from io import open
f = open(r"C:\Users\Sistemas\Desktop\18-11\ejemplo2.txt","w")
f.write("Linea1 \nLinea2 \nLinea3")
f.close()