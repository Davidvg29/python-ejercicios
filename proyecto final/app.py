from tkinter import *

listaAlumnos=[[43501432, "David Valdez Gramajo", ]]
listaMovimientos = [[1, 43501432, "11/11/2024", "14:30", "17:00", "Micro cine"]]
# ----------------INICIO FRONTEND----------------

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
titulo.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
window.grid_columnconfigure(0, weight=1)
# window.grid_rowconfigure(0, weight=1)
# fin titulo

subtitle = Label(window, text="Ultimos movimientos:", font=("Verdana",10))
subtitle.grid(row=1, column=0, padx=10, pady=10,sticky="w")

#inicio titulo de tabla de ultimos movimientos
dniLabel = Label(window, text="DNI", font=("Verdana",10))
dniLabel.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

nombreLabel = Label(window, text="Nombre", font=("Verdana",10))
nombreLabel.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

fechaLabel = Label(window, text="Fecha", font=("Verdana",10))
fechaLabel.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

horaEntadaLabel = Label(window, text="Hora entrada", font=("Verdana",10))
horaEntadaLabel.grid(row=2, column=3, padx=10, pady=10, sticky="nsew")

horaSalidaLabel = Label(window, text="Hora salida", font=("Verdana",10))
horaSalidaLabel.grid(row=2, column=4, padx=10, pady=10, sticky="nsew")

areaUtilizadaLabel = Label(window, text="Area utilizada", font=("Verdana",10))
areaUtilizadaLabel.grid(row=2, column=5, padx=10, pady=10, sticky="nsew")
#fin titulo tablla de ultimos movimientos

#inicio contenido de tabla de ultimos movimientos
dniEntry = Label(window, text="43501432", font=("Verdana",10))
dniEntry.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

nombreEntry = Label(window, text="David Valdez Gramajo", font=("Verdana",10))
nombreEntry.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

fechaEntry = Label(window, text="11/11/2024", font=("Verdana",10))
fechaEntry.grid(row=3, column=2, padx=10, pady=10, sticky="nsew")

horaEntadaEntry = Label(window, text="14:30", font=("Verdana",10))
horaEntadaEntry.grid(row=3, column=3, padx=10, pady=10, sticky="nsew")

horaSalidaEntry = Label(window, text="17:00", font=("Verdana",10))
horaSalidaEntry.grid(row=3, column=4, padx=10, pady=10, sticky="nsew")

areaUtilizadaEntry = Label(window, text="micro cine", font=("Verdana",10))
areaUtilizadaEntry.grid(row=3, column=5, padx=10, pady=10, sticky="nsew")
#fin contenido tabla de ultimos movimientos

# ----------------FIN FRONTEND----------------

window.config(menu = menu)
window.mainloop()
