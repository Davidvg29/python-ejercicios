from tkinter import *

listaAlumnos=[
    [43501432, "David Valdez Gramajo", "vallistos 200v m6 c21", "Banda del Rio Sali", "Tucuman", 3813965671, "Masculino", "29/07/2001", "sin observacion", "david@gmail.com"],
    [84757575, "Juan Mora", "vallistos 200v m6 c21", "Yerba Buena", "Tucuman", 3813123471, "Masculino", "29/07/2001", "sin observacion", "juan@gmail.com"],
    [123, "Javier Milei", "vallistos 200v m6 c21", "Yerba Buena", "Tucuman", 3813123471, "Masculino", "29/07/2001", "sin observacion", "juan@gmail.com"]
]
listaMovimientos = [
    [1, 43501432, "11/11/2024", "14:30", "17:00", "Micro cine"],
    [2, 84757575, "15/11/2024", "15:30", "17:00", "Entretenimiento"],
    [3, 123, "35/11/2024", "27:30", "19:00", "capacitacion"],
]


# def exit():
    # window.destroy()

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
        dniEntry = Label(window, text=listaMovimientos[cont][1], font=("Verdana",10))
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
    
def mostrarAlumnos():
    #muestra las tablas de ultimos movimientos
    windowAlumnos = Tk()
    windowAlumnos.title("Alumnos")
    windowAlumnos.geometry("1200x600")
    windowAlumnos.resizable(0,0)

    # mostrarMenus(windowAlumnos)
    menu = Menu(windowAlumnos)
    menuExit = Menu(menu, tearoff=0)
    menuExit.add_command(label="Volver atras", command=windowAlumnos.destroy)
    menu.add_cascade(label="Opciones", menu=menuExit)
    windowAlumnos.config(menu=menu)

    subtitle = Label(windowAlumnos, text="Alumnos:", font=("Verdana",10))
    subtitle.grid(row=0, column=0, padx=10, pady=10,sticky="w")

    #inicio titulo de tabla de Alumnos
    dniLabel = Label(windowAlumnos, text="DNI", font=("Verdana",10), bg="grey")
    dniLabel.grid(row=1, column=0, padx=0, pady=10, sticky="nsew",)

    nombreLabel = Label(windowAlumnos, text="Nombre", font=("Verdana",10), bg="grey")
    nombreLabel.grid(row=1, column=1, padx=0, pady=10, sticky="nsew",)

    DomicilioLabel = Label(windowAlumnos, text="Domicilio", font=("Verdana",10), bg="grey")
    DomicilioLabel.grid(row=1, column=2, padx=0, pady=10, sticky="nsew",)

    LocalidadLabel = Label(windowAlumnos, text="Localidad", font=("Verdana",10), bg="grey")
    LocalidadLabel.grid(row=1, column=3, padx=0, pady=10, sticky="nsew",)

    provinciaLabel = Label(windowAlumnos, text="Provincia", font=("Verdana",10), bg="grey")
    provinciaLabel.grid(row=1, column=4, padx=0, pady=10, sticky="nsew",)

    TelefonoLabel = Label(windowAlumnos, text="Telefono", font=("Verdana",10), bg="grey")
    TelefonoLabel.grid(row=1, column=5, padx=0, pady=10, sticky="nsew",)

    generoLabel = Label(windowAlumnos, text="Genero", font=("Verdana",10), bg="grey")
    generoLabel.grid(row=1, column=6, padx=0, pady=10, sticky="nsew",)

    fechaNacimientoLabel = Label(windowAlumnos, text="Nacimiento", font=("Verdana",10), bg="grey")
    fechaNacimientoLabel.grid(row=1, column=7, padx=0, pady=10, sticky="nsew",)

    observacionLabel = Label(windowAlumnos, text="Observacion", font=("Verdana",10), bg="grey")
    observacionLabel.grid(row=1, column=8, padx=0, pady=10, sticky="nsew",)

    emailLabel = Label(windowAlumnos, text="Email", font=("Verdana",10), bg="grey")
    emailLabel.grid(row=1, column=9, padx=0, pady=10, sticky="nsew",)

    #inicio contenido de tabla de Alumnos
    cont=0
    while cont < len(listaAlumnos):
        dniLabel = Label(windowAlumnos, text=listaAlumnos[cont][0], font=("Verdana",10))
        dniLabel.grid(row=cont+3, column=0, padx=0, pady=5, sticky="nsew")

        nombreLabel = Label(windowAlumnos, text=listaAlumnos[cont][1], font=("Verdana",10))
        nombreLabel.grid(row=cont+3, column=1, padx=0, pady=5, sticky="nsew")

        DomicilioLabel = Label(windowAlumnos, text=listaAlumnos[cont][2], font=("Verdana",10))
        DomicilioLabel.grid(row=cont+3, column=2, padx=0, pady=5, sticky="nsew")

        LocalidadLabel = Label(windowAlumnos, text=listaAlumnos[cont][3], font=("Verdana",10))
        LocalidadLabel.grid(row=cont+3, column=3, padx=0, pady=5, sticky="nsew")

        provinciaLabel = Label(windowAlumnos, text=listaAlumnos[cont][4], font=("Verdana",10))
        provinciaLabel.grid(row=cont+3, column=4, padx=0, pady=5, sticky="nsew")

        TelefonoLabel = Label(windowAlumnos, text=listaAlumnos[cont][5], font=("Verdana",10))
        TelefonoLabel.grid(row=cont+3, column=5, padx=0, pady=5, sticky="nsew")

        generoLabel = Label(windowAlumnos, text=listaAlumnos[cont][6], font=("Verdana",10))
        generoLabel.grid(row=cont+3, column=6, padx=0, pady=5, sticky="nsew")

        fechaNacimientoLabel = Label(windowAlumnos, text=listaAlumnos[cont][7], font=("Verdana",10))
        fechaNacimientoLabel.grid(row=cont+3, column=7, padx=0, pady=5, sticky="nsew")

        observacionLabel = Label(windowAlumnos, text=listaAlumnos[cont][8], font=("Verdana",10))
        observacionLabel.grid(row=cont+3, column=8, padx=0, pady=5, sticky="nsew")

        emailLabel = Label(windowAlumnos, text=listaAlumnos[cont][9], font=("Verdana",10))
        emailLabel.grid(row=cont+3, column=9, padx=0, pady=5, sticky="nsew")
        cont+=1

    # Configuración de pesos para columnas
    windowAlumnos.grid_columnconfigure(0, weight=1)
    windowAlumnos.grid_columnconfigure(1, weight=1)
    windowAlumnos.grid_columnconfigure(2, weight=1)
    windowAlumnos.grid_columnconfigure(3, weight=1)
    windowAlumnos.grid_columnconfigure(4, weight=1)
    windowAlumnos.grid_columnconfigure(5, weight=1)
    windowAlumnos.grid_columnconfigure(6, weight=1)
    windowAlumnos.grid_columnconfigure(7, weight=1)
    windowAlumnos.grid_columnconfigure(8, weight=1)
    # window.grid_rowconfigure(0, weight=1)
    windowAlumnos.mainloop()

def vistaAñadirAlumno():
    windowAñadirAlumno = Tk()
    windowAñadirAlumno.title("Añadir Alumno")
    windowAñadirAlumno.geometry("900x600")
    windowAñadirAlumno.resizable(0,0)

    menu = Menu(windowAñadirAlumno)
    menuExit = Menu(menu, tearoff=0)
    menuExit.add_command(label="Volver atras", command=windowAñadirAlumno.destroy)
    menu.add_cascade(label="Opciones", menu=menuExit)
    windowAñadirAlumno.config(menu=menu)

    # titulo
    titulo = Label(windowAñadirAlumno, text="Completa el formulario para añadir nuevo alumno", font=("Verdana",15,"bold"))
    titulo.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

    dniLabel = Label(windowAñadirAlumno, text="DNI:", font=("Verdana", 10))
    dniLabel.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
    dniEntry = Entry(windowAñadirAlumno)
    dniEntry.grid(row=2,column=0,padx=5,pady=5, sticky="")

    nameLabel = Label(windowAñadirAlumno, text="Nombre:", font=("Verdana", 10))
    nameLabel.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
    nameEntry = Entry(windowAñadirAlumno)
    nameEntry.grid(row=2,column=1,padx=5,pady=5, sticky="")

    # domicilioLabel = Label(windowAñadirAlumno, text="Domicilio:", font=("Verdana", 10))
    # domicilioLabel.grid(row=5, column=0, columnspan=6, padx=5, pady=5, sticky="nsew")
    # domicilioEntry = Entry(windowAñadirAlumno)
    # domicilioEntry.grid(row=6,column=0,padx=5,pady=5)

    # localidadLabel = Label(windowAñadirAlumno, text="Localidad:", font=("Verdana", 10))
    # localidadLabel.grid(row=7, column=0, columnspan=6, padx=5, pady=5, sticky="nsew")
    # localidadEntry = Entry(windowAñadirAlumno)
    # localidadEntry.grid(row=8,column=0,padx=5,pady=5)

    # provinciaLabel = Label(windowAñadirAlumno, text="Provincia:", font=("Verdana", 10))
    # provinciaLabel.grid(row=9, column=0, columnspan=6, padx=5, pady=5, sticky="nsew")
    # provinciaEntry = Entry(windowAñadirAlumno)
    # provinciaEntry.grid(row=10,column=0,padx=5,pady=5)

    # telefonoLabel = Label(windowAñadirAlumno, text="Telefono:", font=("Verdana", 10))
    # telefonoLabel.grid(row=11, column=0, columnspan=6, padx=5, pady=5, sticky="nsew")
    # telefonoEntry = Entry(windowAñadirAlumno)
    # telefonoEntry.grid(row=12,column=0,padx=5,pady=5)

    # generoLabel = Label(windowAñadirAlumno, text="Genero:", font=("Verdana", 10))
    # generoLabel.grid(row=13, column=0, columnspan=6, padx=5, pady=5, sticky="nsew")
    # generoEntry = Entry(windowAñadirAlumno)
    # generoEntry.grid(row=14,column=0,padx=5,pady=5)

    # fechaNacLabel = Label(windowAñadirAlumno, text="Nacimiento:", font=("Verdana", 10))
    # fechaNacLabel.grid(row=15, column=0, columnspan=6, padx=5, pady=5, sticky="nsew")
    # fechaNacEntry = Entry(windowAñadirAlumno)
    # fechaNacEntry.grid(row=16,column=0,padx=5,pady=5)

    # observacionLabel = Label(windowAñadirAlumno, text="Observacion:", font=("Verdana", 10))
    # observacionLabel.grid(row=17, column=0, columnspan=6, padx=5, pady=5, sticky="nsew")
    # observacionEntry = Entry(windowAñadirAlumno)
    # observacionEntry.grid(row=18,column=0,padx=5,pady=5)

    # mailLabel = Label(windowAñadirAlumno, text="Mail:", font=("Verdana", 10))
    # mailLabel.grid(row=1, column=0, columnspan=6, padx=5, pady=5, sticky="nsew")
    # mailEntry = Entry(windowAñadirAlumno)
    # mailEntry.grid(row=2,column=0,padx=5,pady=5)

    windowAñadirAlumno.grid_columnconfigure(0, weight=1)
    windowAñadirAlumno.grid_columnconfigure(1, weight=1)

    # windowAñadirAlumno.grid_rowconfigure(0, weight=1)
    # windowAñadirAlumno.grid_rowconfigure(1, weight=1)

    windowAñadirAlumno.mainloop()

# configuracion ventana principal
window = Tk()
window.title("Control asistencia")
window.geometry("900x600")
window.resizable(0,0)
# fin configuracion ventana principal

def mostrarMenus(window):
    menu = Menu(window)

    # menu alumnos
    menuAlumnos = Menu(menu, tearoff=0)
    menuAlumnos.add_command(label="Ver todos", command=mostrarAlumnos)
    menuAlumnos.add_command(label="Añadir", command=vistaAñadirAlumno)
    menuAlumnos.add_command(label="Modificar")
    menuAlumnos.add_command(label="Eliminar")
    menu.add_cascade(label="Alumnos", menu=menuAlumnos)
    # fin menu alumnos

    # menu movimientos
    menuMovimientos = Menu(window, tearoff=0)
    # menuMovimientos.add_command(label="Ver todos")
    menuMovimientos.add_command(label="Añadir")
    menuMovimientos.add_command(label="Modificar")
    menuMovimientos.add_command(label="Eliminar")
    menu.add_cascade(label="Movimientos", menu=menuMovimientos)
    # fin menu movimientos

    menuExit = Menu(menu, tearoff=0)
    menuExit.add_command(label="Salir", command=menu.quit)
    menu.add_cascade(label="Opciones", menu=menuExit)

    window.config(menu = menu)

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
mostrarMenus(window)

# ----------------FIN FRONTEND----------------

# window.config(menu = menu)
window.mainloop()
