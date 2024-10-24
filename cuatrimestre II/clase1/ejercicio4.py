from tkinter import *

w = Tk()
w.resizable(0,0)
w.geometry("300x300")
w.config(bg="red")

ft = Frame(w)
ft.pack(side="top", fill="x")
ft.config(bg="red")

fTop = Frame(ft)
fTop.config(bg="green", width="130", height="140")
fTop.pack(side="right", anchor="nw")

fTop2 = Frame(ft)
fTop2.config(bg="green", width="130", height="140")
fTop2.pack(side="left", anchor="ne")

fBottom = Frame(w)
fBottom.config(bg="green", width="300", height="140")
fBottom.pack(side="bottom", anchor="s", fill="x")

w.mainloop()