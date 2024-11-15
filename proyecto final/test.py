listaAlumnos=[
    [43501432, "David Valdez Gramajo", "vallistos 200v m6 c21", "Banda del Rio Sali", "Tucuman", 3813965671, "Masculino", "29/07/2001", "sin observacion", "david@gmail.com"],
    [84757575, "Juan Mora", "vallistos 200v m6 c21", "Yerba Buena", "Tucuman", 3813123471, "Masculino", "29/07/2001", "sin observacion", "juan@gmail.com"],
    [123, "Javier Milei", "vallistos 200v m6 c21", "Yerba Buena", "Tucuman", 3813123471, "Masculino", "29/07/2001", "sin observacion", "juan@gmail.com"]
]
listaMovimientos = [
    [1, 43501432, "11/11/2024", "14:30", "17:00", "Micro cine"],
    [2, 84757575, "15/11/2024", "15:30", "17:00", "Entretenimiento"],
    [3, 123, "35/11/2024", "27:30", "19:00", "capacitacion"]
]

nombre = ""
cont = 0
while len(listaAlumnos) > cont:
    lista = listaAlumnos[cont]
    if 84757575 in lista:
        nombre = listaAlumnos[cont][1]
        break
    cont+=1
print(nombre)