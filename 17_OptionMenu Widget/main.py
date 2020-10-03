from tkinter import *

master = Tk()
master.iconbitmap(r"C:/Users/Juliao JM/Downloads/py-white.ico")
master.title("OptionMenu Widget")
master.geometry("600x400")

def user_choose():
	print("user chose " + str(var.get()))

date_estudent = ["john","mary","clara","clement"]

var = StringVar()
var.set(date_estudent[0]) # to initialize

option = OptionMenu(master, var,*date_estudent)
option.pack()


b = Button(master, text="OK", bg="blue", fg="white", command=user_choose)
b.pack(pady=5)


master.mainloop()