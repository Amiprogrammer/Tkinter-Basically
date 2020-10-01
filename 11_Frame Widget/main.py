from tkinter import *

master = Tk()
master.iconbitmap(r"C:/Users/Juliao JM/Downloads/py-white.ico")
master.title("Frame Widget")
master.geometry("800x600")

separator = Frame(master, bd=1, height=2, relief=GROOVE)

lb1 = Label(master, text="Text 1")
lb2 = Label(master, text="Text 2")

lb1.pack()
separator.pack(fill=X, expand=1)
lb2.pack()

master.mainloop()