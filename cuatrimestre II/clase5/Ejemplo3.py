#   Pida al usuario un texto y almacenelo en un archivo llamod ejemplo3.txt

from io import open
f = open(r"C:\Users\Sistemas\Desktop\18-11\ejemplo3.txt","w")
texto = input("Hola ingresa un texto: ")
f.write(texto)
f.close()