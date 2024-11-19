
from tk import *
from tkinter import ttk
import tkinter as tk
from tkinter import *


main_windows = Tk()
main_windows.config(width=300,height=200)
main_windows.title("Combobox")

combo = ttk.Combobox(state="readonly")
combo.place(x = 50, y = 50)
combo["values"] = ("Opcion1","Opcion2","Opcion3","producto1")
combo.current(3)

main_windows.mainloop()


def pepito(nombre):
    print(nombre)


valor = input("nombre: ")
command =  pepito(valor)