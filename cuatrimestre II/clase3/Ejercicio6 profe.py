from tkinter import *

#   Declaracion de las funciones

def agregar_personal():
    print("Funcion para agregar personal")

def borrar_personal():
    print("Funcion para borrar personal")

def actualizar_datos_personal():
    print("Funcion para actualizar datos de personal")

def salir():
    root.quit()

#   Crear la ventana principal

root = Tk()
root.title("Ventana Administrador")
root.geometry("400x600")

menu_bar = Menu(root)

menu_administrador = Menu(menu_bar,tearoff=0)
menu_administrador.add_command(label="Agregar personal",command=agregar_personal)
menu_administrador.add_command(label="Borrar personal",command=borrar_personal)
menu_administrador.add_command(label="Actualizar datos de personal",command=actualizar_datos_personal)
menu_administrador.add_separator()
menu_administrador.add_command(label="Salir",command=salir)

menu_bar.add_cascade(label="Administrador",menu=menu_administrador)

root.config(menu=menu_bar)

root.mainloop()
