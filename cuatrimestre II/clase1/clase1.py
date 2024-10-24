from tkinter import *

windows = Tk()
windows.title("Hello world") #titulo de ventada
windows.geometry("700x500") #width y heigth de la ventana
windows.resizable(0,0) #tamaño de ventada en x,y. 0 no cambia, 1 si
windows.config(bg="gold") #cambia de color a la ventana
windows.config(relief="ridge", borderwidth="20") #borde de ventana

label=Label(windows, text="Hola mundo", fg="red", bg="green", font=("Verdana", 15, "bold")) #agrega texto con su config
label.place(x="200", y="300") #posicion de texto
label.grid(row=0, column=0, padx=10, pady=10) #grid como en css, padx es padding x y pady es padding y

label=Entry(windows, width="20") #input de texto, el width cambia de tamaño
label.grid(row=0, column=1) #posicion en grid del texto

frame = Frame(windows) #crea un frame, una pantalla dentro de la ventana principal
# frame.pack(side="bottom", anchor="w", fill="x") #empaqueta horizontal posicion del frame en ventana
# frame.pack(side="bottom", anchor="w", fill="y", expand="true") #posiciona verticalmente
frame.config(bg="red")
frame.config(width="200", height="200")

windows.mainloop() #esto siempre va al final