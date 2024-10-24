from tkinter import *

w = Tk()
w.geometry("300x300")
w.resizable(0,0)
w.config(bg="red")

f1 = Frame(w)
f1.config(width=150, height=150)
f1.config(bg="green")
f1.pack(side="top", anchor="e")

f2 = Frame(w)
f2.config(width=150, height=150)
f2.config(bg="green")
f2.pack(side="bottom", anchor="w")

w.mainloop()