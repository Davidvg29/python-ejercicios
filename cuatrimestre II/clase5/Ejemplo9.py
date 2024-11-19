from tkinter import *
from tkinter import messagebox

#   Crear la ventana principal

main_windows = Tk()
main_windows.geometry("300x200")
main_windows.title("MessageBox Ejemplo")

#   Funcion que muestra el messagebox

def mostrar_mensaje():

    messagebox.showinfo("Titulo del mensaje","Este es un mensaje de informacion")

#   Crear un boton para llamar la funcion

boton = Button(main_windows,text="Mostrar el mensaje",command=mostrar_mensaje)
boton.pack(pady=50)

main_windows.mainloop()

