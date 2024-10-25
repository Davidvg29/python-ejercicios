from tkinter import *


lista = []

def guardar():
    lista.append(inputNombre.get())
    lista.append(inputApellido.get())
    lista.append(inputCelular.get())
    # print(lista)

def buscar():
    if inputCelular2.get() in lista:
        posicion = lista.index(inputCelular2.get())
        print(f"Nombre: {lista[posicion-2]}")
        print(f"Apellido: {lista[posicion-1]}")
        print(f"Celular: {lista[posicion]}")
    else:
        print("Usuario no valido")

windows = Tk()
windows.title("Menu")
windows.geometry("700x400")
windows.config(bg="gold")
windows.resizable(0,0)

labelNombre = Label(windows, text="Nombre", fg="black", bg="gold", font=("Verdana", 15, "bold"))
# labelNombre.place(x="200", y="200")
labelNombre.grid(row=0, column=0, padx=20, pady=20, sticky="w")
inputNombre= Entry(windows, width="70")
inputNombre.grid(row=0, column=1, sticky="w")

labelApellido = Label(windows, text="Apellido", fg="black", bg="gold", font=("Verdana", 15, "bold"))
# labelApellido.place(x="200", y="200")
labelApellido.grid(row=1, column=0, padx=20, pady=20, sticky="w")
inputApellido= Entry(windows, width="70")
inputApellido.grid(row=1, column=1, sticky="")

labelCelular = Label(windows, text="Celular", fg="black", bg="gold", font=("Verdana", 15, "bold"))
# labelNombre.place(x="200", y="200")
labelCelular.grid(row=3, column=0, padx=20, pady=20, sticky="w")
inputCelular= Entry(windows, width="70")
inputCelular.grid(row=3, column=1, sticky="w")

enviar1 = Button(windows, text="Enviar", bg="red", font=("Verdana", 15, "bold"), command=guardar)
enviar1.grid(row=4, column=1, sticky="e")

labelCelular2 = Label(windows, text="Buscar celular", fg="black", bg="gold", font=("Verdana", 15, "bold"))
# labelNombre.place(x="200", y="200")
labelCelular2.grid(row=5, column=0, padx=20, pady=20, sticky="w")
inputCelular2= Entry(windows, width="70")
inputCelular2.grid(row=5, column=1, sticky="w")

enviar2 = Button(windows, text="Enviar", bg="green", font=("Verdana", 15, "bold"), command=buscar)
enviar2.grid(row=6, column=1, sticky="e")

windows.mainloop()