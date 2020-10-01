from tkinter import *

master = Tk()
master.iconbitmap(r"C:/Users/Juliao JM/Downloads/py-white.ico")
master.title("Canvas Widget")
master.geometry("600x400")

draw = Canvas(master, width=200, height=100)
draw.pack(fill=BOTH)

draw.create_line(0,100,200,0)
draw.create_line(0,0,200,100,fill="red",dash=(4,4))
draw.create_rectangle(150,75,50,25,fill="blue")

master.mainloop()