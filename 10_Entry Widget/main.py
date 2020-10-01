from tkinter import *

master = Tk()
master.iconbitmap("C:/Users/Juliao JM/Downloads/py-white.ico")
master.title("Entry Widget")
master.geometry("600x400")

e = Entry(master)
e.pack(pady=20)

e.delete(0, END)
e.insert(0, "a default value!")
e.delete(0, END)

master.mainloop()