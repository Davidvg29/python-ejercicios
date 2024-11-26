
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import *


main_windows = Tk()
main_windows.config(width=300,height=200)
main_windows.title("Combobox")

combo = ttk.Combobox(state="readonly")
combo.place(x = 50, y = 50)
combo["values"] = ("Masculino","Femenino")
combo.current(0)


valor = combo.get()
print(valor)
main_windows.mainloop()