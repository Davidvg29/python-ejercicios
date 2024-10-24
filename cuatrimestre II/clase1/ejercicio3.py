from tkinter import *

w = Tk()
w.geometry("300x300")
w.resizable(0,0)
w.config(bg="red")

f = Frame(w)
f.config(bg="green")
f.config(width="80", height="150")
f.pack(side="top", anchor="e")

f1 = Frame(w)
f1.config(bg="green")
f1.config(width="80", height="150")
f1.pack(side="bottom", anchor="w")

w.mainloop()