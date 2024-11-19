import os # sistema operativo
import ast

# f = open(r"E:\Cosas para pc\Programacion\python-ejercicios\proyecto final\test.txt", "w")
# f.write("[]")

new = [235, "asdasd", "bbbb"]
lista = None
f = open(r"E:\Cosas para pc\Programacion\python-ejercicios\proyecto final\test.txt", "r")
lista = ast.literal_eval(f.read())
print(lista)

lista.append(new)

f = open(r"E:\Cosas para pc\Programacion\python-ejercicios\proyecto final\test.txt", "w")
f.write(str(lista))
print(lista[3])
f.close()

