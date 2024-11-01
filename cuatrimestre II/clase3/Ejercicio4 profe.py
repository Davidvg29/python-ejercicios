from tkinter import *

#   Crear la ventana

root = Tk()
root.title("Ventana con menu")
root.geometry("400x600")

#   Crear la barra de menu
menu_bar = Menu(root)

#   Menu 1

menu1 = Menu(menu_bar,tearoff=0) 
menu1.add_command(label="Opcion1")
menu1.add_command(label="Opcion2")
menu1.add_command(label="Opcion3")
menu1.add_separator()
menu1.add_command(label="Opcion4")

#   Agregar el menu a la barra de menu
menu_bar.add_cascade(label="Menu1",menu=menu1)

#   Menu 2

menu2 = Menu(menu_bar,tearoff=0) 
menu2.add_command(label="Opcion5")
menu2.add_command(label="Opcion6")
menu2.add_command(label="Opcion7")
#menu2.add_separator()
menu2.add_command(label="Opcion8")

#   Agregar el menu a la barra de menu
menu_bar.add_cascade(label="Menu2",menu=menu2)

#   Menu 3

menu3 = Menu(menu_bar,tearoff=0) 
menu3.add_command(label="Opcion9")
menu3.add_command(label="Opcion10")
menu3.add_command(label="Opcion11")
#menu2.add_separator()
menu3.add_command(label="Opcion12")

#   Agregar el menu a la barra de menu
menu_bar.add_cascade(label="Menu3",menu=menu3)

#   Configura la barrar de menu en la ventana
root.config(menu=menu_bar)


root.mainloop()