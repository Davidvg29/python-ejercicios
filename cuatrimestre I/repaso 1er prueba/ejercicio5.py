# 5- Dado una lista de N entero positivo presentar en pantalla una nueva lista que contiene los elementos de la lista original que no estén repetidos junto a lista original.

listaOriginal = []
listaNoRepetidos = []

num = int(input("ingrese un numero (0 para terminar): "))
while num !=0:
    listaOriginal.append(num)
    num = int(input("ingrese un numero (0 para terminar): "))
for i in listaOriginal:
    if i not in listaNoRepetidos:
        listaNoRepetidos.append(i) 

print("lista original: ", listaOriginal)
print("lista no repetidos ", listaNoRepetidos)