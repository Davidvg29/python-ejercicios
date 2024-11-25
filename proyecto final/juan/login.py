#900x600 pantalla del login 
#usuario y contraseña para ingresar en el sistema de asistencia 

import tkinter as tk
from tkinter import messagebox


def verificar_credenciales():
    usuario_ingresado = usuario_entry.get()
    contrasena_ingresada = contrasena_entry.get()

    if usuario_ingresado == "admin" and contrasena_ingresada == "12345":
        messagebox.showinfo("Éxito", "Bienvenido al sistema de asistencia!")
    else:
        messagebox.showerror("Error", "Usuario o contraseña no válidos.")

ventana = tk.Tk()

ventana.title("Login sistema de asistencia")
ventana.geometry("900x600+200+100") 

# img = tk.PhotoImage(file="C:\Users\Punto Digital\Downloads\logo.png")
img = tk.PhotoImage(file="C:\\Users\\Punto Digital\\Downloads\\logo.png")
lbl_img = tk.Label(ventana, image = img)
lbl_img.pack() 

usuario_label = tk.Label(ventana, text="Usuario")
usuario_label.pack()

contrasena_label = tk.Label(ventana, text="Contraseña:")
contrasena_label.pack()

usuario_entry = tk.Entry(ventana)
usuario_entry.pack()

contrasena_entry = tk.Entry(ventana, show="*")
contrasena_entry.pack()

boton_iniciar_sesion = tk.Button(ventana, text="Iniciar Sesión", command=verificar_credenciales)
boton_iniciar_sesion.pack()

ventana.mainloop()