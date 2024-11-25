from tkinter import *

AcercaDe = Tk() 

AcercaDe.title("Acerca de: Sistema de Asistencia") # Titulo de la ventana
AcercaDe.geometry("600x400+200+50") # Tamaño de la ventana
AcercaDe.config(bg="gray") # Color de la ventana

lbl1 = Label(AcercaDe , text= "Sistema de Asistencia")
lbl1.pack() 
lbl2 = Label(AcercaDe , text= "Versión 1.0")
lbl2.pack() 
lbl3 = Label(AcercaDe , text= "Desarrollado por David Valdez Gramajo y Juan Mora")
lbl3.pack() 
lbl4 = Label(AcercaDe , text= "Prof. José Francisco Fernández – Programación II – UTN")
lbl4.pack() 
lbl5 = Label(AcercaDe , text= "La licencia de este producto es libre para ser usado en los Punto Digitales de la Rep. Argentina")
lbl5.pack() 
lbl6 = Label(AcercaDe , text= "Gracias por elegir nuestro Sistema de Asistencia")
lbl6.pack() 
lbl7 = Label(AcercaDe , text= "Consultas: bandadelriosali@puntodigital.gob.ar")
lbl7.pack() 

AcercaDe.iconbitmap("E:\\Cosas para pc\\Programacion\\python-ejercicios\\proyecto final\\juan\\asistencia.ico") #Icono del Sistema
AcercaDe.mainloop()