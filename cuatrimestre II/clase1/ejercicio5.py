from tkinter import *

w = Tk()
w.geometry("300x300")
w.config(bg="green")

canvas = Canvas(w, width=300, height=300, bg="green")
canvas.pack()

canvas.create_line(0, 0, 300, 300, fill="red", width=20)
canvas.create_line(300, 0, 0, 300, fill="red", width=20)

w.mainloop()