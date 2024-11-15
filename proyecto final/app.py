from tkinter import *

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
# ----------------INICIO FRONTEND----------------

#funciones frontend
def mostrarTablaUltimosMovimientos(listaMovimientos):
    #muestra las tablas de ultimos movimientos
    subtitle = Label(window, text="Ultimos movimientos:", font=("Verdana",10))
    subtitle.grid(row=1, column=0, padx=10, pady=10,sticky="w")

    #inicio titulo de tabla de ultimos movimientos
    dniLabel = Label(window, text="DNI", font=("Verdana",10), bg="grey")
    dniLabel.grid(row=2, column=0, padx=0, pady=10, sticky="nsew",)

    nombreLabel = Label(window, text="Nombre", font=("Verdana",10), bg="grey")
    nombreLabel.grid(row=2, column=1, padx=0, pady=10, sticky="nsew")

    fechaLabel = Label(window, text="Fecha", font=("Verdana",10), bg="grey")
    fechaLabel.grid(row=2, column=2, padx=0, pady=10, sticky="nsew")

    horaEntadaLabel = Label(window, text="Hora entrada", font=("Verdana",10), bg="grey")
    horaEntadaLabel.grid(row=2, column=3, padx=0, pady=10, sticky="nsew")

    horaSalidaLabel = Label(window, text="Hora salida", font=("Verdana",10), bg="grey")
    horaSalidaLabel.grid(row=2, column=4, padx=0, pady=10, sticky="nsew")

    areaUtilizadaLabel = Label(window, text="Area utilizada", font=("Verdana",10), bg="grey")
    areaUtilizadaLabel.grid(row=2, column=5, padx=0, pady=10, sticky="nsew")
    #fin titulo tablla de ultimos movimientos

    #inicio contenido de tabla de ultimos movimientos
    contadorListaMovimientos = len(listaMovimientos)
    cont = 0
    row=3
    while cont < contadorListaMovimientos:
        dniEntry = Label(window, text=listaMovimientos[cont][1], font=("Verdana",10), bg="red")
        dniEntry.grid(row=row, column=0, padx=0, pady=5, sticky="nsew")

        nombre = ""
        cont2 = 0
        while len(listaAlumnos) > cont2:
            lista = listaAlumnos[cont2]
            if listaMovimientos[cont][1] in lista:
                nombre = listaAlumnos[cont2][1]
                break
            cont2+=1
        nombreEntry = Label(window, text=nombre, font=("Verdana",10))
        nombreEntry.grid(row=row, column=1, padx=0, pady=5, sticky="nsew")

        fechaEntry = Label(window, text=listaMovimientos[cont][2], font=("Verdana",10))
        fechaEntry.grid(row=row, column=2, padx=0, pady=5, sticky="nsew")

        horaEntadaEntry = Label(window, text=listaMovimientos[cont][3], font=("Verdana",10))
        horaEntadaEntry.grid(row=row, column=3, padx=0, pady=5, sticky="nsew")

        horaSalidaEntry = Label(window, text=listaMovimientos[cont][4], font=("Verdana",10))
        horaSalidaEntry.grid(row=row, column=4, padx=0, pady=5, sticky="nsew")

        areaUtilizadaEntry = Label(window, text=listaMovimientos[cont][5], font=("Verdana",10))
        areaUtilizadaEntry.grid(row=row, column=5, padx=0, pady=5, sticky="nsew")
        #fin contenido tabla de ultimos movimientos
        
        row+=1
        cont+=1

#fin funcion mostrar tablas
    
# configuracion ventana principal
window = Tk()
window.title("Control asistencia")
window.geometry("900x600")
window.resizable(0,0)
# fin configuracion ventana principal

menu = Menu(window)

# menu alumnos
menuAlumnos = Menu(menu, tearoff=0)
menuAlumnos.add_command(label="Agregar")
menu.add_cascade(label="Alumnos", menu=menuAlumnos)
# fin menu alumnos

# menu movimientos
menuMovimientos = Menu(window, tearoff=0)
menuMovimientos.add_command(label="Añadir")
menuMovimientos.add_command(label="Modificar")
menuMovimientos.add_command(label="Eliminar")
menu.add_cascade(label="Movimientos", menu=menuMovimientos)
# fin menu movimientos

# titulo
titulo = Label(window, text="Bienvenido al sistema de asistencias", font=("Verdana",15,"bold"))
titulo.grid(row=0, column=0, columnspan=6, padx=20, pady=20, sticky="nsew")
# fin titulo

# Configuración de pesos para columnas
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_columnconfigure(3, weight=1)
window.grid_columnconfigure(4, weight=1)
window.grid_columnconfigure(5, weight=1)
# window.grid_rowconfigure(0, weight=1)

mostrarTablaUltimosMovimientos(listaMovimientos)

# ----------------FIN FRONTEND----------------

window.config(menu = menu)
window.mainloop()
