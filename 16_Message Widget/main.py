from tkinter import *

master = Tk()
master.iconbitmap(r"C:/Users/Juliao JM/Downloads/py-white.ico")
master.title("Message Widget")
master.geometry("600x400")

m = Message(master, text="This is a message!")
m.pack()

separator = Frame(master, height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X)

m2 = Message(master, text="This is a long Message, if you read you will tired!", width=190)
m2.pack()

master.mainloop()