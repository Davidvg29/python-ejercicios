#   Creacion de la lista para usar en la comparacion
listaLetras = list("abcdefghijklmnñopqrstuvwxyz")
#print(len(listaLetras))3

# Definicion de las funciones
def numeroLetra():                  #   Boton llama a la funcion
                                    #   Lee (captura) el numero del entry y lo convierte en letra
    #   Lo hago mal de entrada y luego lo corregimos <---- Borrar ese error
    valor = int(entryNumero.get())
    entryNumero.delete(0,"end")
    if 1 <= valor <= 27:
        labelLetra = Label(windows,text=listaLetras[valor-1])
        labelLetra.grid(row=4,column=1,padx=10,pady=10)
    else:
        labelLetra = Label(windows,text="El valor no existe")
        labelLetra.grid(row=4,column=1,padx=10,pady=10)
        
# Programa principal

from tkinter import *

windows = Tk()
windows.geometry("300x180")
windows.title("Numero a letra")

labelNumero = Label(windows,text="Ingrese un numero del 1 al 27",font=("Verdana",12,"bold"))
labelNumero.grid(row=1,column=1,padx=10,pady=10)

entryNumero = Entry(windows)
entryNumero.grid(row=2,column=1,padx=10,pady=10)

botonNumero = Button(windows,text="Enviar",bg="red",command=numeroLetra)

botonNumero.grid(row=3,column=1,padx=10,pady=10)

windows.mainloop() #    Siempre al final

