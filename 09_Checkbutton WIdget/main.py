from tkinter import *

master = Tk()
master.iconbitmap(r"C:/Users/Juliao JM/Downloads/py-white.ico")
master.title("Checkbutton Widget")
master.geometry("600x400")

def user_chose():
	print("user chose " + var.get())

var = StringVar()

x1 = Checkbutton(master, text="python", variable=var, onvalue="python", offvalue=None)
x2 = Checkbutton(master, text="java", variable=var, onvalue="java", offvalue=None)
b = Button(master, text="Ok", command=user_chose)

x1.pack()
x2.pack()
b.pack()

master.mainloop()