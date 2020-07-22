from tkinter import *

master = Tk()
master.title("jm")
master.iconbitmap(r"C:\Users\Juliao JM\Downloads\all-icons\py.ico")

top = Toplevel()
top.title("about this program")
top.iconbitmap(r"C:\Users\Juliao JM\Downloads\all-icons\py.ico")

m = Message(top, text="this program built with tkinter 8.5", font=("Source Code Pro",12))
m.pack()

b = Button(top)
b["text"] = "Dismiss"
b["fg"] = "white"
b["bg"] = "red"
b["command"] = top.destroy
b.pack()


master.mainloop()