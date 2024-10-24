from tkinter import *

windows=Tk()
windows.config(bg="red")
w.resizable(0,0)
windows.geometry("200x200")

frame=Frame(windows)
frame.config(bg="blue")
frame.pack(side="bottom", fill="x")
frame.config(width="100", height="100")

windows.mainloop()