from tkinter import *
from tkinter import ttk
import ast
import os
from tkinter import messagebox
import random
import matplotlib.pyplot as plt #instalar libreria pip install matplotlib

# listaAlumnos = [
#         [43501432, "David Valdez Gramajo", "vallistos 200v m6 c21", "Banda del Rio Sali", "Tucuman", 3813965671, "Masculino", "29/07/2001", "sin observacion", "david@gmail.com"],
#         [84757575, "Juan Mora", "vallistos 200v m6 c21", "Yerba Buena", "Tucuman", 3813123471, "Masculino", "29/07/2001", "sin observacion", "juan@gmail.com"],
#         [123, "Javier Milei", "vallistos 200v m6 c21", "Yerba Buena", "Tucuman", 3813123471, "Masculino", "29/07/2001", "sin observacion", "juan@gmail.com"]
#     ]

# listaMovimientos = [
#         [1, 43501432, "11/11/2024", "14:30", "17:00", "Micro cine"],
#         [2, 84757575, "15/11/2024", "15:30", "17:00", "Entretenimiento"],
#         [3, 123, "35/11/2024", "27:30", "19:00", "capacitacion"]
#     ]

rutaBase = os.path.dirname(__file__)
rutaArchivoAlumnos = os.path.join(rutaBase, "alumnos.txt")
rutaArchivoMovimientos = os.path.join(rutaBase, "movimientos.txt")
rutaImgIconoAsistencia = os.path.join(rutaBase, "asistencia.ico")
rutaImgLogoPD = os.path.join(rutaBase, "logoPD.png")
rutaGraficoEstadisticaGenero = os.path.join(rutaBase, "graficoEstadisticaGeneros.png")
rutaGraficoEstadisticaAreaUtilizada = os.path.join(rutaBase, "graficoEstadisticaAreaUtilizadas.png")

def traerInfoAlumnos():
    # rutaArchivoAlumnos = r"E:\Cosas para pc\Programacion\python-ejercicios\proyecto final\alumnos.txt"
    global rutaArchivoAlumnos
    listaAlumnos=[]

    if os.path.exists(rutaArchivoAlumnos):
        with open(rutaArchivoAlumnos,"r") as f:
            contentAlumnos = ast.literal_eval(f.read())
            print(contentAlumnos)
            return contentAlumnos
    else:
        print("Archivo ALUMNOS no creado")
        f = open(rutaArchivoAlumnos,"w")
        f.write(str(listaAlumnos))
        f.close()
        return listaAlumnos

def traerInfoMovimientos():
    global rutaArchivoMovimientos
    # rutaArchivoMovimientos = r"E:\Cosas para pc\Programacion\python-ejercicios\proyecto final\movimientos.txt"
    listaMovimientos = []

    if os.path.exists(rutaArchivoMovimientos):
        with open(rutaArchivoMovimientos,"r") as f:
            contentMovimientos = ast.literal_eval(f.read())
            print(contentMovimientos)
            return contentMovimientos
    else:
        print("Archivo MOVIMIENTOS no creado")
        f = open(rutaArchivoMovimientos,"w")
        f.write(str(listaMovimientos))
        f.close()
        return listaMovimientos

def guardarAlumno(nuevoAlumno):
    global listaAlumnos
    f = open(rutaArchivoAlumnos, "r")
    listaAlumnos = ast.literal_eval(f.read())
    listaAlumnos.append(nuevoAlumno)
    f = open(rutaArchivoAlumnos, "w")
    f.write(str(listaAlumnos))
    f.close()

def guardarMovimientos(nuevoMovimiento):
    global listaMovimientos
    f = open(rutaArchivoMovimientos, "r")
    listaMovimientos = ast.literal_eval(f.read())
    listaMovimientos.append(nuevoMovimiento)
    f = open(rutaArchivoMovimientos, "w")
    f.write(str(listaMovimientos))
    f.close()

listaAlumnos = traerInfoAlumnos()

listaMovimientos = traerInfoMovimientos()

# ----------------FUNCIONES LOGICAS----------------

def encriptacion(texto):
    listaLetras = list("abcdefghijklmnñopqrstuvwxyz")
    valor = 5
    mezcla = listaLetras[27-valor:] + listaLetras[:27-valor]
    # mezclaInvertida = listaLetras[-(27 - valor):] + listaLetras[:-(27 - valor)]

    # texto = "admin"
    textoEncriptado = "vyhdi"
    # encriptacion
    textoEncriptadoAux = ""
    cont=0
    while len(texto) > cont:
        if texto[cont] in listaLetras:
            indice = listaLetras.index(texto[cont])
            textoEncriptadoAux+=mezcla[indice]
            # print(f"{texto[cont]}, corresponde, {mezcla[indice]}")
        cont+=1
    if textoEncriptadoAux == textoEncriptado:
        return True
    else:
        return False

    # desencriptacion
    # def desencriptacion():
    #     cont2=0
    #     while len(textoEncriptado) > cont2:
    #         if textoEncriptado[cont2] in mezcla:
    #             indice = mezcla.index(textoEncriptado[cont2])
    #             print(f"{textoEncriptado[cont2]}, corresponde, {listaLetras[indice]}")
    #         cont2 += 1

def logicaAñadirAlumno():
    global dniEntry, nameEntry, domicilioEntry, localidadEntry, provinciaEntry, telefonoEntry, generoEntry, fechaNacEntry, observacionEntry, mailEntry, mensajeErrorAñadirAlumno
    error=""
    generoEntry = comboboxGenero
    def validacion():
        global error
        error = ""
        if dniEntry.get() == "":
            error = "DNI no puede estar vacio"
            return error
        if not dniEntry.get().isdigit():
            error = "DNI no puede ser letras"
            return error
        if nameEntry.get()== "":
            error = "Por favor complete NOMBRE"
            return error
        if domicilioEntry.get()== "":
            error = "Por favor complete DOMICILIO"
            return error
        if localidadEntry.get()== "":
            error = "Por favor complete LOCALIDAD"
            return error
        if provinciaEntry.get()== "":
            error = "Por favor complete PROVINCIA"
            return error
        if telefonoEntry.get()== "":
            error = "Por favor complete TELEFONO"
            return error
        if not telefonoEntry.get().isdigit():
            error = "TELEFONO no puede ser letras"
            return error
        if generoEntry.get()== "":
            error = "Por favor complete GENERO"
            return error
        if fechaNacEntry.get()== "":
            error = "Por favor complete NACIMIENTO"
            return error
        if mailEntry.get()== "":
            error = "Por favor complete MAIL"
            return error
        return ""
    validacion = validacion()
    if validacion == "":
    # while verifica si exite el alumno con el dni ingresado
        cont=0
        while cont < len(listaAlumnos):
            if int(dniEntry.get()) == listaAlumnos[cont][0]:  
                error = "El alumno ya se encuentra registrado"
                mensajeErrorAñadirAlumno.config(text=error, fg="red")
                return
            cont += 1
        nuevoAlumno = [
        int(dniEntry.get()), 
        nameEntry.get(), 
        domicilioEntry.get(), 
        localidadEntry.get(), 
        provinciaEntry.get(), 
        int(telefonoEntry.get()), 
        generoEntry.get(),
        fechaNacEntry.get(),
        observacionEntry.get(),
        mailEntry.get()
        ]
        # listaAlumnos.append(nuevoAlumno)
        guardarAlumno(nuevoAlumno)
        error = "Alumno registrado correctamente"
        mensajeErrorAñadirAlumno.config(text=error, fg="green")
    else:
        mensajeErrorAñadirAlumno.config(text=validacion, fg="red")
def logicaModificarAlumno(dniEntry, nameEntry, domicilioEntry, localidadEntry, provinciaEntry, telefonoEntry, generoEntry, fechaNacEntry, observacionEntry, mailEntry, mensajeErrorAñadirAlumno):
    error=""
    generoEntry = comboboxGenero
    def validacion():
        global error
        error = ""
        if dniEntry.get() == "":
            error = "DNI no puede estar vacio"
            return error
        if not dniEntry.get().isdigit():
            error = "DNI no puede ser letras"
            return error
        if nameEntry.get()== "":
            error = "Por favor complete NOMBRE"
            return error
        if domicilioEntry.get()== "":
            error = "Por favor complete DOMICILIO"
            return error
        if localidadEntry.get()== "":
            error = "Por favor complete LOCALIDAD"
            return error
        if provinciaEntry.get()== "":
            error = "Por favor complete PROVINCIA"
            return error
        if telefonoEntry.get()== "":
            error = "Por favor complete TELEFONO"
            return error
        if not telefonoEntry.get().isdigit():
            error = "TELEFONO no puede ser letras"
            return error
        if generoEntry.get()== "":
            error = "Por favor complete GENERO"
            return error
        if fechaNacEntry.get()== "":
            error = "Por favor complete NACIMIENTO"
            return error
        if mailEntry.get()== "":
            error = "Por favor complete MAIL"
            return error
        return ""
    validacion = validacion()
    if validacion != "":
        mensajeErrorAñadirAlumno.config(text=validacion, fg="red")
        return
    else:
        infoAlumActualizar = []
        cont=0
        while len(listaAlumnos) > cont:
            if str(dniEntry.get()) == str(listaAlumnos[cont][0]):
                infoAlumActualizar= listaAlumnos[cont]
                listaAlumnos[cont][1] = nameEntry.get()
                listaAlumnos[cont][2] = domicilioEntry.get()
                listaAlumnos[cont][3] = localidadEntry.get()
                listaAlumnos[cont][4] = provinciaEntry.get()
                listaAlumnos[cont][5] = telefonoEntry.get()
                listaAlumnos[cont][6] = generoEntry.get()
                listaAlumnos[cont][7] = fechaNacEntry.get()
                listaAlumnos[cont][8] = observacionEntry.get()
                listaAlumnos[cont][9] = mailEntry.get()
            cont+=1

        if len(infoAlumActualizar) > 0:
            f = open(rutaArchivoAlumnos,"w")
            f.write(str(listaAlumnos))
            f.close()
            mensajeErrorAñadirAlumno.config(text="Alumno actualizado", fg="green")
def logicaEliminarAlumno(dniEntry, mensajeErrorEliminarAlumno, windowEliminarAlumno):
    cont = 0
    alumnoEliminado = False
    while len(listaAlumnos) > cont:
        if str(listaAlumnos[cont][0]) == str(dniEntry.get()):
            listaAlumnos.remove(listaAlumnos[cont])
            f = open(rutaArchivoAlumnos,"w")
            f.write(str(listaAlumnos))
            f.close()
            alumnoEliminado = True
            messagebox.showinfo(message="Alumno eliminado...", title="Eliminacion correcta")
            windowEliminarAlumno.destroy()
        cont+=1
    if not alumnoEliminado:
        mensajeErrorEliminarAlumno.config(text="Alumno no encontrado", fg="red")

def validacionMovimiento(dniEntry, fechaEntry, horaEntradaEntry, horaSalidaEntry, comboboxAreaUtilizada, mensajeErrorAñadirMovimiento):
    error = ""
    alumnoEncontrado = False
    cont = 0
    while len(listaAlumnos) > cont:
        if str(listaAlumnos[cont][0]) == str(dniEntry.get()):
            alumnoEncontrado = True
            break 
        cont+=1
    if not alumnoEncontrado:
        mensajeErrorAñadirMovimiento.config(text="Alumno no registrado, primero registra el alumno")
        return
    else:
        if len(fechaEntry.get()) < 1:
            error = "Fecha no puede estar vacia"
        elif len(horaEntradaEntry.get()) < 1:
            error = "Hora de entrada no puede estar vacia"
        elif len(horaSalidaEntry.get()) < 1:
            error = "Hora de salida no puede estar vacia"
        elif len(comboboxAreaUtilizada.get()) < 1:
            error = "Area utilizada no puede estar vacia"
    mensajeErrorAñadirMovimiento.config(text=error)
    return error

def validacionModificarMovimiento(idEntry, dniEntry, fechaEntry, horaEntradaEntry, horaSalidaEntry, comboboxAreaUtilizada, mensajeErrorModificarMovimiento):
    error = ""
    if len(fechaEntry.get()) < 1:
        error = "Fecha no puede estar vacia"
    elif len(horaEntradaEntry.get()) < 1:
        error = "Hora de entrada no puede estar vacia"
    elif len(horaSalidaEntry.get()) < 1:
        error = "Hora de salida no puede estar vacia"
    elif len(comboboxAreaUtilizada.get()) < 1:
        error = "Area utilizada no puede estar vacia"
    mensajeErrorModificarMovimiento.config(text=error)
    return error

def logicaAñadirMovimiento(idEntry, dniEntry, fechaEntry, horaEntradaEntry, horaSalidaEntry, comboboxAreaUtilizada, mensajeErrorAñadirMovimiento, windowAñadirMovimiento):
    global listaMovimientos
    validacion = validacionMovimiento(dniEntry, fechaEntry, horaEntradaEntry, horaSalidaEntry, comboboxAreaUtilizada, mensajeErrorAñadirMovimiento)
    if validacion == "":
        nuevoMovimiento = [
            int(idEntry.get()),
            int(dniEntry.get()),
            fechaEntry.get(), 
            horaEntradaEntry.get(), 
            horaSalidaEntry.get(), 
            comboboxAreaUtilizada.get()
        ]
        guardarMovimientos(nuevoMovimiento)
        print("linea 261")
        messagebox.showinfo("Movimiento añadido", "El nuevo movimiento fue añadido correctamente")
        mostrarTablaUltimosMovimientos(listaMovimientos)
        windowAñadirMovimiento.destroy()
    else:
        mensajeErrorAñadirMovimiento.config(text=validacion, fg="red")

def logicaModificarMovimiento(idEntry, dniEntry, fechaEntry, horaEntradaEntry, horaSalidaEntry, comboboxAreaUtilizada, mensajeError, mensajeErrorModificarMovimiento, windowModificarMovimiento):
    validacion = validacionModificarMovimiento(idEntry, dniEntry, fechaEntry, horaEntradaEntry, horaSalidaEntry, comboboxAreaUtilizada, mensajeErrorModificarMovimiento)
    if validacion != "":
        mensajeErrorModificarMovimiento.config(text=validacion, fg="red")
        return
    else:
        infoMovimientoActualizar = []
        cont=0
        while len(listaMovimientos) > cont:
            if str(idEntry.get()) == str(listaMovimientos[cont][0]):
                infoMovimientoActualizar= listaMovimientos[cont]
                listaMovimientos[cont][1] = int(dniEntry.get())
                listaMovimientos[cont][2] = fechaEntry.get()
                listaMovimientos[cont][3] = horaEntradaEntry.get()
                listaMovimientos[cont][4] = horaSalidaEntry.get()
                listaMovimientos[cont][5] = comboboxAreaUtilizada.get()
            cont+=1

        if len(infoMovimientoActualizar) > 0:
            f = open(rutaArchivoMovimientos,"w")
            f.write(str(listaMovimientos))
            f.close()
            mensajeErrorModificarMovimiento.config(text="Movimiento actualizado", fg="green")
            mostrarTablaUltimosMovimientos(listaMovimientos)
            messagebox.showinfo("Modificar movimiento", "Movimiento modificado con exito")
            windowModificarMovimiento.destroy()
    
def logicaEliminarMovimiento(idEntry, mensajeErrorEliminarMovimiento, windowEliminarMovimiento):
    movimientoEliminado = False  # Bandera para verificar si se eliminó un movimiento

    # Iterar sobre la lista de movimientos
    cont = 0
    while len(listaMovimientos) > cont:
        if str(listaMovimientos[cont][0]) == str(idEntry):  # Comparar ID como cadenas
            listaMovimientos.pop(cont)  # Eliminar el movimiento de la lista

            # Guardar la lista actualizada en el archivo
            with open(rutaArchivoMovimientos, "w") as f:
                f.write(str(listaMovimientos))
            
            movimientoEliminado = True  # Marcar como eliminado

            # Actualizar la tabla
            mostrarTablaUltimosMovimientos(listaMovimientos)

            # Mostrar mensaje de éxito y cerrar ventana
            messagebox.showinfo(message="Movimiento eliminado...", title="Eliminación correcta")
            windowEliminarMovimiento.destroy()
            break  # Terminar el bucle una vez eliminado
        cont += 1

    # Si no se encontró el movimiento, mostrar mensaje de error
    if not movimientoEliminado:
        mensajeErrorEliminarMovimiento.config(text="Movimiento no encontrado", fg="red")

def verEstadisticaGenero():
    global rutaGraficoEstadisticaGenero
    numMasculinos = 0
    numFemeninos = 0

    if len(listaAlumnos) > 0:
        cont = 0
        while len(listaAlumnos) > cont:
            if listaAlumnos[cont][6] == "Masculino" or listaAlumnos[cont][6] == "masculino":
                numMasculinos+=1
            elif listaAlumnos[cont][6] == "Femenino" or listaAlumnos[cont][6] == "femenino":
                numFemeninos+=1
            cont+=1
        fix, ax = plt.subplots()
        ax.set_title("Estadistica por generos")
        ax.pie([numMasculinos,numFemeninos], labels=["Masculinos", "Femeninos"], autopct='%1.1f%%', colors=["lightblue", "pink"])
        plt.savefig(rutaGraficoEstadisticaGenero)
        plt.show()
    else:
        messagebox.showinfo(message="Estadisticas no disponibles... No hay alumnos.", title="Estadisticas")

def verEstadisticaAreasUtilizadas():
    numEntretenimiento = 0
    numCapacitacion = 0
    numMicrocine = 0

    if len(listaMovimientos) > 0:
        cont = 0
        while len(listaMovimientos) > cont:
            if listaMovimientos[cont][5] == "Entretenimiento":
                numEntretenimiento+=1
            elif listaMovimientos[cont][5] == "Capacitacion":
                numCapacitacion+=1
            else:
                numMicrocine+=1
            cont+=1
        fix, ax = plt.subplots()
        ax.bar(["Entretenimiento","Capacitacion","Microcine"],
            [numEntretenimiento,numCapacitacion,numMicrocine])
        max_valor = max([numEntretenimiento,numCapacitacion,numMicrocine])  # Máximo valor de las barras
        ax.set_yticks(range(0, max_valor + 2))
        plt.savefig(rutaGraficoEstadisticaAreaUtilizada)
        plt.show()
    else:
        messagebox.showinfo(message="Estadisticas no disponibles... No hay movimientos.", title="Estadisticas")


# ----------------FIN FUNCIONES LOGICAS----------------

# ----------------INICIO FRONTEND----------------

#funciones frontend
def mostrarTablaUltimosMovimientos(listaMovimientos):

    for widget in window.grid_slaves():
            if int(widget.grid_info()["row"]) >= 1:  # Solo limpiar las filas de la tabla
                widget.destroy()

    subtitle = Label(window, text="Ultimos movimientos:", font=("Verdana",10))
    subtitle.grid(row=1, column=0, padx=10, pady=10,sticky="w")
    if len(listaMovimientos) > 0:
        #muestra las tablas de ultimos movimientos

        #inicio titulo de tabla de ultimos movimientos
        idMovimientoLabel = Label(window, text="ID", font=("Verdana",10), bg="grey")
        idMovimientoLabel.grid(row=2, column=0, padx=0, pady=10, sticky="nsew",)

        dniLabel = Label(window, text="DNI", font=("Verdana",10), bg="grey")
        dniLabel.grid(row=2, column=1, padx=0, pady=10, sticky="nsew",)

        nombreLabel = Label(window, text="Nombre", font=("Verdana",10), bg="grey")
        nombreLabel.grid(row=2, column=2, padx=0, pady=10, sticky="nsew")

        fechaLabel = Label(window, text="Fecha", font=("Verdana",10), bg="grey")
        fechaLabel.grid(row=2, column=3, padx=0, pady=10, sticky="nsew")

        horaEntadaLabel = Label(window, text="Hora entrada", font=("Verdana",10), bg="grey")
        horaEntadaLabel.grid(row=2, column=4, padx=0, pady=10, sticky="nsew")

        horaSalidaLabel = Label(window, text="Hora salida", font=("Verdana",10), bg="grey")
        horaSalidaLabel.grid(row=2, column=5, padx=0, pady=10, sticky="nsew")

        areaUtilizadaLabel = Label(window, text="Area utilizada", font=("Verdana",10), bg="grey")
        areaUtilizadaLabel.grid(row=2, column=6, padx=0, pady=10, sticky="nsew")
        #fin titulo tablla de ultimos movimientos

        #inicio contenido de tabla de ultimos movimientos
        contadorListaMovimientos = len(listaMovimientos)
        cont = 0
        row=3
    
        while cont < contadorListaMovimientos:
            idEntry = Label(window, text=listaMovimientos[cont][0], font=("Verdana",10))
            idEntry.grid(row=row, column=0, padx=0, pady=5, sticky="nsew")

            dniEntry = Label(window, text=listaMovimientos[cont][1], font=("Verdana",10))
            dniEntry.grid(row=row, column=1, padx=0, pady=5, sticky="nsew")

            nombre = ""
            cont2 = 0
            if len(listaAlumnos) > 0:
                while len(listaAlumnos) > cont2:
                    lista = listaAlumnos[cont2]
                    if listaMovimientos[cont][1] in lista:
                        nombre = listaAlumnos[cont2][1]
                        break
                    cont2+=1
            else:
                return
            nombreEntry = Label(window, text=nombre, font=("Verdana",10))
            nombreEntry.grid(row=row, column=2, padx=0, pady=5, sticky="nsew")

            fechaEntry = Label(window, text=listaMovimientos[cont][2], font=("Verdana",10))
            fechaEntry.grid(row=row, column=3, padx=0, pady=5, sticky="nsew")

            horaEntadaEntry = Label(window, text=listaMovimientos[cont][3], font=("Verdana",10))
            horaEntadaEntry.grid(row=row, column=4, padx=0, pady=5, sticky="nsew")

            horaSalidaEntry = Label(window, text=listaMovimientos[cont][4], font=("Verdana",10))
            horaSalidaEntry.grid(row=row, column=5, padx=0, pady=5, sticky="nsew")

            areaUtilizadaEntry = Label(window, text=listaMovimientos[cont][5], font=("Verdana",10))
            areaUtilizadaEntry.grid(row=row, column=6, padx=0, pady=5, sticky="nsew")
            #fin contenido tabla de ultimos movimientos
            
            row+=1
            cont+=1
    else:
        subtitle = Label(window, text="Sin movimientos...", font=("Verdana",10))
        subtitle.grid(row=2, column=0, padx=10, pady=10,sticky="w")
    #fin funcion mostrar tablas
    
def mostrarAlumnos():
    #muestra las tablas de ultimos movimientos
    windowAlumnos = Tk()
    windowAlumnos.title("Alumnos")
    windowAlumnos.geometry("1200x600+100+50")
    windowAlumnos.resizable(0,0)

    # mostrarMenus(windowAlumnos)
    menu = Menu(windowAlumnos)
    menuExit = Menu(menu, tearoff=0)
    menuExit.add_command(label="Volver atras", command=windowAlumnos.destroy)
    menu.add_cascade(label="Opciones", menu=menuExit)
    windowAlumnos.config(menu=menu)

    subtitle = Label(windowAlumnos, text="Alumnos:", font=("Verdana",10))
    subtitle.grid(row=0, column=0, padx=10, pady=10,sticky="w")

    if len(listaAlumnos) > 0:
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
    else:
        subtitle = Label(windowAlumnos, text="sin Alumnos", font=("Verdana",10))
        subtitle.grid(row=2, column=0, padx=10, pady=10,sticky="w")
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
    windowAlumnos.iconbitmap(rutaImgIconoAsistencia)
    windowAlumnos.mainloop()

dniEntry = None
nameEntry = None
domicilioEntry = None
localidadEntry = None
provinciaEntry = None
telefonoEntry = None
generoEntry = None
fechaNacEntry = None
observacionEntry = None
mailEntry = None
mensajeErrorAñadirAlumno = None
def vistaAñadirAlumno():
    global dniEntry, nameEntry, domicilioEntry, localidadEntry, provinciaEntry, telefonoEntry, generoEntry, fechaNacEntry, observacionEntry, mailEntry, mensajeErrorAñadirAlumno

    windowAñadirAlumno = Tk()
    windowAñadirAlumno.title("Añadir Alumno")
    windowAñadirAlumno.geometry("900x600+200+50")
    windowAñadirAlumno.resizable(0,0)

    windowAñadirAlumno.iconbitmap(rutaImgIconoAsistencia)


    menu = Menu(windowAñadirAlumno)
    menuExit = Menu(menu, tearoff=0)
    menuExit.add_command(label="Volver atras", command=windowAñadirAlumno.destroy)
    menu.add_cascade(label="Opciones", menu=menuExit)
    windowAñadirAlumno.config(menu=menu)

    # titulo
    titulo = Label(windowAñadirAlumno, text="Completa el formulario para añadir nuevo alumno", font=("Verdana",15,"bold"))
    titulo.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

    # label y entry de dni
    dniLabel = Label(windowAñadirAlumno, text="DNI:", font=("Verdana", 10))
    dniLabel.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
    dniEntry = Entry(windowAñadirAlumno, width="30")
    dniEntry.grid(row=2,column=0,padx=5,pady=5, sticky="")

    # label y entry de nombre
    nameLabel = Label(windowAñadirAlumno, text="Nombre:", font=("Verdana", 10))
    nameLabel.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
    nameEntry = Entry(windowAñadirAlumno, width="30")
    nameEntry.grid(row=2,column=1,padx=5,pady=5, sticky="")

    domicilioLabel = Label(windowAñadirAlumno, text="Domicilio:", font=("Verdana", 10))
    domicilioLabel.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
    domicilioEntry = Entry(windowAñadirAlumno, width="30")
    domicilioEntry.grid(row=4,column=0,padx=5,pady=5)

    localidadLabel = Label(windowAñadirAlumno, text="Localidad:", font=("Verdana", 10))
    localidadLabel.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
    localidadEntry = Entry(windowAñadirAlumno, width="30")
    localidadEntry.grid(row=4,column=1,padx=5,pady=5)

    provinciaLabel = Label(windowAñadirAlumno, text="Provincia:", font=("Verdana", 10))
    provinciaLabel.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")
    provinciaEntry = Entry(windowAñadirAlumno, width="30")
    provinciaEntry.grid(row=6,column=0,padx=5,pady=5)

    telefonoLabel = Label(windowAñadirAlumno, text="Telefono:", font=("Verdana", 10))
    telefonoLabel.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")
    telefonoEntry = Entry(windowAñadirAlumno, width="30")
    telefonoEntry.grid(row=6,column=1,padx=5,pady=5)

    generoLabel = Label(windowAñadirAlumno, text="Genero:", font=("Verdana", 10))
    generoLabel.grid(row=7, column=0, padx=5, pady=5, sticky="nsew")
    # generoEntry = Entry(windowAñadirAlumno, width="30")
    # generoEntry.grid(row=8,column=0,padx=5,pady=5)

    global comboboxGenero
    comboboxGenero = ttk.Combobox(windowAñadirAlumno, state="readonly")
    comboboxGenero.grid(row=8,column=0,padx=5,pady=5)
    comboboxGenero["values"] = ("Masculino","Femenino")
    comboboxGenero.current(0)

    fechaNacLabel = Label(windowAñadirAlumno, text="Nacimiento:", font=("Verdana", 10))
    fechaNacLabel.grid(row=7, column=1, padx=5, pady=5, sticky="nsew")
    fechaNacEntry = Entry(windowAñadirAlumno, width="30")
    fechaNacEntry.grid(row=8,column=1,padx=5,pady=5)

    observacionLabel = Label(windowAñadirAlumno, text="Observacion:", font=("Verdana", 10))
    observacionLabel.grid(row=9, column=0, padx=5, pady=5, sticky="nsew")
    observacionEntry = Entry(windowAñadirAlumno, width="30")
    observacionEntry.grid(row=10,column=0,padx=5,pady=5)

    mailLabel = Label(windowAñadirAlumno, text="Mail:", font=("Verdana", 10))
    mailLabel.grid(row=9, column=1, padx=5, pady=5, sticky="nsew")
    mailEntry = Entry(windowAñadirAlumno, width="30")
    mailEntry.grid(row=10,column=1,padx=5,pady=5)

    # errorAñadirAlumno = mensajeErrorAñadirAlumno
    mensajeErrorAñadirAlumno = Label(windowAñadirAlumno, text="", fg="red", font=("Verdana", 10))
    mensajeErrorAñadirAlumno.grid(row=11, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

    buttonGuardar = Button(windowAñadirAlumno, command=logicaAñadirAlumno, text="Guardar", fg="white",bg="grey", font=("Verdana", 12, "bold"))
    buttonGuardar.grid(row=12, column=0, columnspan=2, padx=300, pady=20, sticky="nsew")

    windowAñadirAlumno.grid_columnconfigure(0, weight=1)
    windowAñadirAlumno.grid_columnconfigure(1, weight=1)

    # windowAñadirAlumno.grid_rowconfigure(0, weight=1)
    # windowAñadirAlumno.grid_rowconfigure(1, weight=1)

    windowAñadirAlumno.mainloop()

def vistaModificarAlumno():

    windowModificarAlumno = Tk()
    windowModificarAlumno.title("Modificar Alumno")
    windowModificarAlumno.geometry("900x600+200+50")
    windowModificarAlumno.resizable(0,0)

    windowModificarAlumno.iconbitmap(rutaImgIconoAsistencia)


    def buscarALumnoDni():
        if buscarAlumnoDniEntry.get() == "":
            mensajeError.config(text="Campo vacio, ingrese DNI", fg="red")
            return
        if not buscarAlumnoDniEntry.get().isdigit():
            mensajeError.config(text="No puedes ingresar letras, ingrese solo numeros")
            return
        cont = 0
        while len(listaAlumnos) > cont:
            if int(buscarAlumnoDniEntry.get()) == listaAlumnos[cont][0]:
                mensajeError.config(text="Alumno encontrado", fg="green")
                # label y entry de dni
                dniLabel = Label(windowModificarAlumno, text="DNI:", font=("Verdana", 10))
                dniLabel.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
                dniEntry = Entry(windowModificarAlumno, width="30")
                dniEntry.grid(row=2,column=0,padx=5,pady=5, sticky="")
                dniEntry.insert(0, listaAlumnos[cont][0])
                dniEntry.config(state="disabled")

                # label y entry de nombre
                nameLabel = Label(windowModificarAlumno, text="Nombre:", font=("Verdana", 10))
                nameLabel.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
                nameEntry = Entry(windowModificarAlumno, width="30")
                nameEntry.grid(row=2,column=1,padx=5,pady=5, sticky="")
                nameEntry.insert(0, listaAlumnos[cont][1])

                domicilioLabel = Label(windowModificarAlumno, text="Domicilio:", font=("Verdana", 10))
                domicilioLabel.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
                domicilioEntry = Entry(windowModificarAlumno, width="30")
                domicilioEntry.grid(row=4,column=0,padx=5,pady=5)
                domicilioEntry.insert(0, listaAlumnos[cont][2])

                localidadLabel = Label(windowModificarAlumno, text="Localidad:", font=("Verdana", 10))
                localidadLabel.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
                localidadEntry = Entry(windowModificarAlumno, width="30")
                localidadEntry.grid(row=4,column=1,padx=5,pady=5)
                localidadEntry.insert(0, listaAlumnos[cont][3])

                provinciaLabel = Label(windowModificarAlumno, text="Provincia:", font=("Verdana", 10))
                provinciaLabel.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")
                provinciaEntry = Entry(windowModificarAlumno, width="30")
                provinciaEntry.grid(row=6,column=0,padx=5,pady=5)
                provinciaEntry.insert(0, listaAlumnos[cont][4])

                telefonoLabel = Label(windowModificarAlumno, text="Telefono:", font=("Verdana", 10))
                telefonoLabel.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")
                telefonoEntry = Entry(windowModificarAlumno, width="30")
                telefonoEntry.grid(row=6,column=1,padx=5,pady=5)
                telefonoEntry.insert(0, listaAlumnos[cont][5])

                global comboboxGenero
                comboboxGenero = ttk.Combobox(windowModificarAlumno, state="readonly")
                comboboxGenero.grid(row=8,column=0,padx=5,pady=5)
                comboboxGenero["values"] = ("Masculino","Femenino")
                comboboxGenero.current(comboboxGenero["values"].index(listaAlumnos[cont][6]))

                fechaNacLabel = Label(windowModificarAlumno, text="Nacimiento:", font=("Verdana", 10))
                fechaNacLabel.grid(row=7, column=1, padx=5, pady=5, sticky="nsew")
                fechaNacEntry = Entry(windowModificarAlumno, width="30")
                fechaNacEntry.grid(row=8,column=1,padx=5,pady=5)
                fechaNacEntry.insert(0, listaAlumnos[cont][7])

                observacionLabel = Label(windowModificarAlumno, text="Observacion:", font=("Verdana", 10))
                observacionLabel.grid(row=9, column=0, padx=5, pady=5, sticky="nsew")
                observacionEntry = Entry(windowModificarAlumno, width="30")
                observacionEntry.grid(row=10,column=0,padx=5,pady=5)
                observacionEntry.insert(0, listaAlumnos[cont][8])

                mailLabel = Label(windowModificarAlumno, text="Mail:", font=("Verdana", 10))
                mailLabel.grid(row=9, column=1, padx=5, pady=5, sticky="nsew")
                mailEntry = Entry(windowModificarAlumno, width="30")
                mailEntry.grid(row=10,column=1,padx=5,pady=5)
                mailEntry.insert(0, listaAlumnos[cont][9])

                # errorAñadirAlumno = mensajeErrorAñadirAlumno
                mensajeErrorAñadirAlumno = Label(windowModificarAlumno, text="", fg="red", font=("Verdana", 10))
                mensajeErrorAñadirAlumno.grid(row=11, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

                buttonGuardar = Button(windowModificarAlumno, command=lambda: logicaModificarAlumno(dniEntry, nameEntry, domicilioEntry, localidadEntry, provinciaEntry, telefonoEntry, generoEntry, fechaNacEntry, observacionEntry, mailEntry, mensajeError), text="Modificar", fg="white",bg="grey", font=("Verdana", 12, "bold"))
                buttonGuardar.grid(row=12, column=0, columnspan=2, padx=300, pady=20, sticky="nsew")

                windowModificarAlumno.grid_columnconfigure(0, weight=1)
                windowModificarAlumno.grid_columnconfigure(1, weight=1)
                return
            cont+=1
            mensajeError.config(text="Alumno no registrado", fg="red")



    menu = Menu(windowModificarAlumno)
    menuExit = Menu(menu, tearoff=0)
    menuExit.add_command(label="Volver atras", command=windowModificarAlumno.destroy)
    menu.add_cascade(label="Opciones", menu=menuExit)
    windowModificarAlumno.config(menu=menu)

    # titulo
    titulo = Label(windowModificarAlumno, text="Busca por DNI el alumno que desea modificar", font=("Verdana",15,"bold"))
    titulo.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

    buscarAlumnoDniEntry = Entry(windowModificarAlumno, width="30")
    buscarAlumnoDniEntry.grid(row=1,column=0, padx=5,pady=5, sticky="e")
    
    buttonBuscarAlumno = Button(windowModificarAlumno, command=buscarALumnoDni, text="Buscar", fg="white",bg="grey", font=("Verdana", 10, "bold"))
    buttonBuscarAlumno.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    mensajeError = Label(windowModificarAlumno, text="", fg="red", font=("Verdana",10))
    mensajeError.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    windowModificarAlumno.grid_columnconfigure(0, weight=1)
    windowModificarAlumno.grid_columnconfigure(1, weight=1)
    windowModificarAlumno.mainloop()

def vistaEliminarAlumno():
    windowEliminarAlumno = Tk()
    windowEliminarAlumno.title("Eliminar Alumno")
    windowEliminarAlumno.geometry("900x600+200+50")
    windowEliminarAlumno.resizable(0,0)

    windowEliminarAlumno.iconbitmap(rutaImgIconoAsistencia)


    menu = Menu(windowEliminarAlumno)
    menuExit = Menu(menu, tearoff=0)
    menuExit.add_command(label="Volver atras", command=windowEliminarAlumno.destroy)
    menu.add_cascade(label="Opciones", menu=menuExit)
    windowEliminarAlumno.config(menu=menu)

    # titulo
    titulo = Label(windowEliminarAlumno, text="Escribe el DNI de alumno para eliminar: ", font=("Verdana",15,"bold"))
    titulo.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

    # label y entry de dni
    dniLabel = Label(windowEliminarAlumno, text="DNI:", font=("Verdana", 10))
    dniLabel.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
    dniEntry = Entry(windowEliminarAlumno, width="30")
    dniEntry.grid(row=2,column=0,padx=5,pady=5, sticky="")

    buttonEliminarAlumno = Button(windowEliminarAlumno, command=lambda:logicaEliminarAlumno(dniEntry, mensajeErrorEliminarAlumno, windowEliminarAlumno), text="Eliminar", fg="white",bg="grey", font=("Verdana", 10, "bold"))
    buttonEliminarAlumno.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    mensajeErrorEliminarAlumno = Label(windowEliminarAlumno, text="", fg="red", font=("Verdana",10))
    mensajeErrorEliminarAlumno.grid(row=3, column=0,columnspan=1, padx=5, pady=5, sticky="nsew")

    windowEliminarAlumno.grid_columnconfigure(0, weight=1)
    windowEliminarAlumno.grid_columnconfigure(1, weight=1)
    windowEliminarAlumno.mainloop()

def vistaAñadirMovimiento():
    windowAñadirMovimiento = Tk()
    windowAñadirMovimiento.title("Añadir Movimiento")
    windowAñadirMovimiento.geometry("900x600+200+50")
    windowAñadirMovimiento.resizable(0,0)

    windowAñadirMovimiento.iconbitmap(rutaImgIconoAsistencia)


    menu = Menu(windowAñadirMovimiento)
    menuExit = Menu(menu, tearoff=0)
    menuExit.add_command(label="Volver atras", command=windowAñadirMovimiento.destroy)
    menu.add_cascade(label="Opciones", menu=menuExit)
    windowAñadirMovimiento.config(menu=menu)

    # titulo
    titulo = Label(windowAñadirMovimiento, text="Completa el formulario para añadir nuevo movimiento", font=("Verdana",15,"bold"))
    titulo.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

    idLabel = Label(windowAñadirMovimiento, text="ID:", font=("Verdana", 10))
    idLabel.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
    idEntry = Entry(windowAñadirMovimiento, width="30")
    idEntry.grid(row=2,column=0,padx=5,pady=5, sticky="")
    idEntry.insert(0, random.randint(1, 999))
    idEntry.config(state="disabled")

    dniLabel = Label(windowAñadirMovimiento, text="DNI:", font=("Verdana", 10))
    dniLabel.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
    dniEntry = Entry(windowAñadirMovimiento, width="30")
    dniEntry.grid(row=2,column=1,padx=5,pady=5, sticky="")

    # label y entry de nombre
    fechaLabel = Label(windowAñadirMovimiento, text="Fecha:", font=("Verdana", 10))
    fechaLabel.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
    fechaEntry = Entry(windowAñadirMovimiento, width="30")
    fechaEntry.grid(row=4,column=0,padx=5,pady=5, sticky="")

    horaEntradaLabel = Label(windowAñadirMovimiento, text="Hora entrada:", font=("Verdana", 10))
    horaEntradaLabel.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
    horaEntradaEntry = Entry(windowAñadirMovimiento, width="30")
    horaEntradaEntry.grid(row=4,column=1,padx=5,pady=5)

    horaSalidaLabel = Label(windowAñadirMovimiento, text="Hora salida:", font=("Verdana", 10))
    horaSalidaLabel.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")
    horaSalidaEntry = Entry(windowAñadirMovimiento, width="30")
    horaSalidaEntry.grid(row=6,column=0,padx=5,pady=5)

    areaUtilizadaLabel = Label(windowAñadirMovimiento, text="Area utilizada:", font=("Verdana", 10))
    areaUtilizadaLabel.grid(row=5, column=1, padx=100, pady=5, sticky="nsew")
    # areaUtilizadaEntry = Entry(windowAñadirMovimiento, width="30")
    # areaUtilizadaEntry.grid(row=6,column=1,padx=5,pady=5)

    # global comboboxAreaUtilizada
    comboboxAreaUtilizada = ttk.Combobox(windowAñadirMovimiento, state="readonly")
    comboboxAreaUtilizada.grid(row=6, column=1, padx=5, pady=5)
    comboboxAreaUtilizada["values"] = ("Entretenimiento","Capacitacion", "Microcine")
    comboboxAreaUtilizada.current(0)

    buttonGuardar = Button(windowAñadirMovimiento, command=lambda: logicaAñadirMovimiento(idEntry, dniEntry, fechaEntry, horaEntradaEntry, horaSalidaEntry, comboboxAreaUtilizada, mensajeErrorAñadirMovimiento, windowAñadirMovimiento), text="Guardar", fg="white",bg="grey", font=("Verdana", 12, "bold"))
    buttonGuardar.grid(row=8, column=0, columnspan=2, padx=300, pady=20, sticky="nsew")
    
    mensajeErrorAñadirMovimiento = Label(windowAñadirMovimiento, text="", fg="red", font=("Verdana", 10))
    mensajeErrorAñadirMovimiento.grid(row=7, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")


    windowAñadirMovimiento.grid_columnconfigure(0, weight=1)
    windowAñadirMovimiento.grid_columnconfigure(1, weight=1)

    windowAñadirMovimiento.mainloop()

def vistaModificarMovimiento():
    windowModificarMovimiento = Tk()
    windowModificarMovimiento.title("Modificar Alumno")
    windowModificarMovimiento.geometry("900x600+200+50")
    windowModificarMovimiento.resizable(0,0)

    windowModificarMovimiento.iconbitmap(rutaImgIconoAsistencia)


    def buscarMovimientoId():
        if buscarMovimientoIdEntry.get() == "":
            mensajeError.config(text="Campo vacio, ingrese ID", fg="red")
            return
        if not buscarMovimientoIdEntry.get().isdigit():
            mensajeError.config(text="No puedes ingresar letras, ingrese solo numeros")
            return
        cont = 0
        while len(listaMovimientos) > cont:
            if int(buscarMovimientoIdEntry.get()) == listaMovimientos[cont][0]:
                mensajeError.config(text="Movimiento encontrado", fg="green")
                idLabel = Label(windowModificarMovimiento, text="ID:", font=("Verdana", 10))
                idLabel.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
                idEntry = Entry(windowModificarMovimiento, width="30")
                idEntry.grid(row=2,column=0,padx=5,pady=5, sticky="")
                idEntry.insert(0, buscarMovimientoIdEntry.get())
                idEntry.config(state="disabled")

                dniLabel = Label(windowModificarMovimiento, text="DNI:", font=("Verdana", 10))
                dniLabel.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
                dniEntry = Entry(windowModificarMovimiento, width="30")
                dniEntry.grid(row=2,column=1,padx=5,pady=5, sticky="")
                dniEntry.insert(0, listaMovimientos[cont][1])
                dniEntry.config(state="disabled")

                # label y entry de nombre
                fechaLabel = Label(windowModificarMovimiento, text="Fecha:", font=("Verdana", 10))
                fechaLabel.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
                fechaEntry = Entry(windowModificarMovimiento, width="30")
                fechaEntry.grid(row=4,column=0,padx=5,pady=5, sticky="")
                fechaEntry.insert(0, listaMovimientos[cont][2])

                horaEntradaLabel = Label(windowModificarMovimiento, text="Hora entrada:", font=("Verdana", 10))
                horaEntradaLabel.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
                horaEntradaEntry = Entry(windowModificarMovimiento, width="30")
                horaEntradaEntry.grid(row=4,column=1,padx=5,pady=5)
                horaEntradaEntry.insert(0, listaMovimientos[cont][3])

                horaSalidaLabel = Label(windowModificarMovimiento, text="Hora salida:", font=("Verdana", 10))
                horaSalidaLabel.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")
                horaSalidaEntry = Entry(windowModificarMovimiento, width="30")
                horaSalidaEntry.grid(row=6,column=0,padx=5,pady=5)
                horaSalidaEntry.insert(0, listaMovimientos[cont][4])

                areaUtilizadaLabel = Label(windowModificarMovimiento, text="Area utilizada:", font=("Verdana", 10))
                areaUtilizadaLabel.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")
                # areaUtilizadaEntry = Entry(windowModificarMovimiento, width="30")
                # areaUtilizadaEntry.grid(row=6,column=1,padx=5,pady=5)
                # areaUtilizadaEntry.insert(0, listaMovimientos[cont][5])

                # global comboboxAreaUtilizada
                comboboxAreaUtilizada = ttk.Combobox(windowModificarMovimiento, state="readonly")
                comboboxAreaUtilizada.grid(row=6,column=1,padx=5,pady=5)
                comboboxAreaUtilizada["values"] = ("Entretenimiento","Capacitacion", "Microcine")
                comboboxAreaUtilizada.current(comboboxAreaUtilizada["values"].index(listaMovimientos[cont][5]))

                mensajeErrorModificarMovimiento = Label(windowModificarMovimiento, text="", fg="red", font=("Verdana", 10))
                mensajeErrorModificarMovimiento.grid(row=8, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

                buttonGuardar = Button(windowModificarMovimiento, command=lambda: logicaModificarMovimiento(idEntry, dniEntry, fechaEntry, horaEntradaEntry, horaSalidaEntry, comboboxAreaUtilizada, mensajeError, mensajeErrorModificarMovimiento, windowModificarMovimiento), text="Guardar", fg="white",bg="grey", font=("Verdana", 12, "bold"))
                buttonGuardar.grid(row=9, column=0, columnspan=2, padx=300, pady=20, sticky="nsew")
                return
            cont+=1
            mensajeError.config(text="Movimiento inexistente", fg="red")

    menu = Menu(windowModificarMovimiento)
    menuExit = Menu(menu, tearoff=0)
    menuExit.add_command(label="Volver atras", command=windowModificarMovimiento.destroy)
    menu.add_cascade(label="Opciones", menu=menuExit)
    windowModificarMovimiento.config(menu=menu)

    # titulo
    titulo = Label(windowModificarMovimiento, text="Busca por ID el movimiento que desea modificar", font=("Verdana",15,"bold"))
    titulo.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

    buscarMovimientoIdEntry = Entry(windowModificarMovimiento, width="30")
    buscarMovimientoIdEntry.grid(row=1,column=0, padx=5,pady=5, sticky="e")
    
    buttonBuscarMovimiento = Button(windowModificarMovimiento, command=buscarMovimientoId, text="Buscar", fg="white",bg="grey", font=("Verdana", 10, "bold"))
    buttonBuscarMovimiento.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    mensajeError = Label(windowModificarMovimiento, text="", fg="red", font=("Verdana",10))
    mensajeError.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    windowModificarMovimiento.grid_columnconfigure(0, weight=1)
    windowModificarMovimiento.grid_columnconfigure(1, weight=1)
    windowModificarMovimiento.mainloop()

def vistaEliminarMovimiento():
    windowEliminarMovimiento = Tk()
    windowEliminarMovimiento.title("Eliminar Movimiento")
    windowEliminarMovimiento.geometry("900x600+200+50")
    windowEliminarMovimiento.resizable(0,0)

    windowEliminarMovimiento.iconbitmap(rutaImgIconoAsistencia)


    menu = Menu(windowEliminarMovimiento)
    menuExit = Menu(menu, tearoff=0)
    menuExit.add_command(label="Volver atras", command=windowEliminarMovimiento.destroy)
    menu.add_cascade(label="Opciones", menu=menuExit)
    windowEliminarMovimiento.config(menu=menu)

    # titulo
    titulo = Label(windowEliminarMovimiento, text="Escribe el ID de Movimiento para eliminar: ", font=("Verdana",15,"bold"))
    titulo.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

    # label y entry de dni
    idLabel = Label(windowEliminarMovimiento, text="ID:", font=("Verdana", 10))
    idLabel.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
    idEntry = Entry(windowEliminarMovimiento, width="30")
    idEntry.grid(row=2,column=0,padx=5,pady=5, sticky="")

    buttonEliminarMovimiento = Button(windowEliminarMovimiento, command=lambda:logicaEliminarMovimiento(idEntry.get(), mensajeErrorEliminarMovimiento, windowEliminarMovimiento), text="Eliminar", fg="white",bg="grey", font=("Verdana", 10, "bold"))
    buttonEliminarMovimiento.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    mensajeErrorEliminarMovimiento = Label(windowEliminarMovimiento, text="", fg="red", font=("Verdana",10))
    mensajeErrorEliminarMovimiento.grid(row=3, column=0,columnspan=1, padx=5, pady=5, sticky="nsew")

    windowEliminarMovimiento.grid_columnconfigure(0, weight=1)
    windowEliminarMovimiento.grid_columnconfigure(1, weight=1)
    windowEliminarMovimiento.mainloop()

def vistaAcercaDe():
    AcercaDe = Tk() 

    AcercaDe.title("Acerca de: Sistema de Asistencia") # Titulo de la ventana
    AcercaDe.geometry("900x600+200+50") # Tamaño de la ventana
    # AcercaDe.config(bg="gray") # Color de la ventana

    menu = Menu(AcercaDe)
    menuExit = Menu(menu, tearoff=0)
    menuExit.add_command(label="Volver atras", command=AcercaDe.destroy)
    menu.add_cascade(label="Opciones", menu=menuExit)
    AcercaDe.config(menu=menu)

    lbl1 = Label(AcercaDe, font=("Verdana",15,"bold"), text= "Sistema de Asistencia")
    lbl1.pack( pady=10) 
    lbl2 = Label(AcercaDe, font=("Verdana",10), text= "Versión 1.0")
    lbl2.pack( pady=10) 
    lbl3 = Label(AcercaDe, font=("Verdana",10), text= "Desarrollado por David Valdez Gramajo y Juan Mora")
    lbl3.pack( pady=10) 
    lbl4 = Label(AcercaDe, font=("Verdana",10), text= "Prof. José Francisco Fernández – Programación II – UTN")
    lbl4.pack( pady=10) 
    lbl5 = Label(AcercaDe, font=("Verdana",10), text= "La licencia de este producto es libre para ser usado en los Punto Digitales de la Rep. Argentina")
    lbl5.pack( pady=10) 
    lbl6 = Label(AcercaDe, font=("Verdana",12), text= "Gracias por elegir nuestro Sistema de Asistencia")
    lbl6.pack( pady=10) 
    lbl7 = Label(AcercaDe, font=("Verdana",12), text= "Consultas: bandadelriosali@puntodigital.gob.ar")
    lbl7.pack( pady=10) 

    AcercaDe.iconbitmap(rutaImgIconoAsistencia) #Icono del Sistema
    AcercaDe.mainloop()

def vistaManual():
    ventanaManual = Tk()
    ventanaManual.title("Manual de usuario:")
    ventanaManual.geometry("900x600+200+50")
    ventanaManual.resizable(0,0)  # Tamaño de la ventana
    # ventanaManual.config(bg="gray")  # Color de la ventana

    menu = Menu(ventanaManual)
    menuExit = Menu(menu, tearoff=0)
    menuExit.add_command(label="Volver atras", command=ventanaManual.destroy)
    menu.add_cascade(label="Opciones", menu=menuExit)
    ventanaManual.config(menu=menu)

    texto= """
    Manual de Usuario: Sistema de Asistencia Punto Digital Banda del Río Salí

    Introducción
    Este manual tiene como objetivo guiarte en el uso del Sistema de Asistencia del Punto Digital Banda del Río Salí. Este sistema está diseñado para registrar de forma eficiente la circulación de alumnos, facilitando la gestión administrativa y brindando datos precisos sobre la asistencia.

    Funcionalidades Principales
    - Registro de alumnos: Ingresar los datos personales de cada alumno (nombre completo, género, etc.).
    - Registro de asistencia: Registrar la fecha, hora de entrada y salida de cada alumno.
    - Generación de reportes: Obtener informes detallados sobre la asistencia de los alumnos, incluyendo:
    - Listado de alumnos por día.
    - Cantidad de alumnos por género.
    - Movimientos mensuales.
    - Consulta de información: Buscar información específica sobre un alumno o un período determinado.

    Soporte Técnico
    En caso de dudas o problemas técnicos, comunícate con el equipo de soporte técnico a través del siguiente correo electrónico: bandadelriosali@puntodigital.gob.ar
    """
    textoLabel = Label(ventanaManual, text=texto, font=("Verdana", 12), wraplength=750, justify="left" )
    textoLabel.pack(padx=20, pady=20)

    # Configurar el ícono del sistema
    ventanaManual.iconbitmap(rutaImgIconoAsistencia)

    ventanaManual.mainloop()

def vistaLogin():
    def verificar_credenciales():
        usuario_ingresado = usuario_entry.get().strip()  # Quita espacios en blanco
        contrasena_ingresada = contrasena_entry.get().strip()

        if len(usuario_ingresado) < 1 or len(contrasena_ingresada) < 1:
            messagebox.showerror("Error", "Completa los campos correspondientes.")  # Campos vacíos
            return

        validacionContraseña = encriptacion(contrasena_ingresada)

        if usuario_ingresado == "admin" and validacionContraseña == True:
            messagebox.showinfo("Exito", "Bienvenido al sistema de asistencia!")
            ventanaLogin.destroy()
            main()
            return

        # Credenciales incorrectas
        messagebox.showerror("Error", "Usuario o contraseña no válidos.")


    ventanaLogin = Tk()
    ventanaLogin.title("Login sistema de asistencia")
    ventanaLogin.geometry("900x600+200+50") 
    ventanaLogin.resizable(0,0)

    # img = tk.PhotoImage(file="C:\Users\Punto Digital\Downloads\logo.png")
    ventanaLogin.iconbitmap(rutaImgIconoAsistencia)

    img = PhotoImage(file=rutaImgLogoPD)
    lbl_img = Label(ventanaLogin, image = img)
    lbl_img.grid(row=0, column=1, columnspan=3, padx=5, pady=5, sticky="nsew") 

    usuario_label = Label(ventanaLogin, text="Usuario")
    usuario_label.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")

    usuario_entry = Entry(ventanaLogin, width=30)
    usuario_entry.grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")

    contrasena_label = Label(ventanaLogin, text="Contraseña:")
    contrasena_label.grid(row=3, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")

    contrasena_entry = Entry(ventanaLogin, show="*", width=30)
    contrasena_entry.grid(row=4, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")

    boton_iniciar_sesion = Button(ventanaLogin, text="Iniciar Sesión", command=verificar_credenciales)
    boton_iniciar_sesion.grid(row=5, column=1, columnspan=3, padx=5, pady=10, sticky="nsew")

    ventanaLogin.grid_columnconfigure(0, weight=1)
    ventanaLogin.grid_columnconfigure(1, weight=0)
    ventanaLogin.grid_columnconfigure(2, weight=0)
    ventanaLogin.grid_columnconfigure(3, weight=0)
    ventanaLogin.grid_columnconfigure(4, weight=1)
    # ventanaLogin.grid_columnconfigure(5, weight=1)
    # ventanaLogin.grid_columnconfigure(6, weight=1)

    ventanaLogin.mainloop()

def main():

    # configuracion ventana principal
    global window
    window = Tk()
    window.title("Control asistencia")
    window.geometry("900x600+200+50")
    # window.resizable(0,0)
    # fin configuracion ventana principal

    # Configuración de pesos para columnas
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    window.grid_columnconfigure(2, weight=1)
    window.grid_columnconfigure(3, weight=1)
    window.grid_columnconfigure(4, weight=1)
    window.grid_columnconfigure(5, weight=1)
    window.grid_columnconfigure(6, weight=1)
    # window.grid_rowconfigure(0, weight=1)

    window.iconbitmap(rutaImgIconoAsistencia)

    mostrarTablaUltimosMovimientos(listaMovimientos)
    mostrarMenus(window)

    # window.config(menu = menu)
    window.mainloop()

def mostrarMenus(window):
    menu = Menu(window)

    # menu alumnos
    menuAlumnos = Menu(menu, tearoff=0)
    menuAlumnos.add_command(label="Ver todos", command=mostrarAlumnos)
    menuAlumnos.add_command(label="Añadir", command=vistaAñadirAlumno)
    menuAlumnos.add_command(label="Modificar", command=vistaModificarAlumno)
    menuAlumnos.add_command(label="Eliminar", command=vistaEliminarAlumno)
    menuAlumnos.add_separator()
    menuAlumnos.add_command(label="Ver estadistica", command=verEstadisticaGenero)
    menu.add_cascade(label="Alumnos", menu=menuAlumnos)
    # fin menu alumnos

    # menu movimientos
    menuMovimientos = Menu(window, tearoff=0)
    # menuMovimientos.add_command(label="Ver todos")
    menuMovimientos.add_command(label="Añadir", command=vistaAñadirMovimiento)
    menuMovimientos.add_command(label="Modificar", command=vistaModificarMovimiento)
    menuMovimientos.add_command(label="Eliminar", command=vistaEliminarMovimiento)
    menuMovimientos.add_separator()
    menuMovimientos.add_command(label="Ver estadisticas areas utilizadas", command=verEstadisticaAreasUtilizadas)
    menu.add_cascade(label="Movimientos", menu=menuMovimientos)
    # fin menu movimientos

    menuExit = Menu(menu, tearoff=0)
    menuExit.add_command(label="Manual", command=vistaManual)
    menuExit.add_command(label="Acerca de", command=vistaAcercaDe)
    menuExit.add_separator()
    menuExit.add_command(label="Salir", command=window.destroy)
    menu.add_cascade(label="Opciones", menu=menuExit)

    window.config(menu = menu)

    # titulo
    titulo = Label(window, text="Bienvenido al sistema de asistencias", font=("Verdana",15,"bold"))
    titulo.grid(row=0, column=0, columnspan=7, padx=20, pady=20, sticky="nsew")
    # fin titulo


vistaLogin()

# ----------------FIN FRONTEND----------------


