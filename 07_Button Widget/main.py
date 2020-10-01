from tkinter import *

master = Tk()
master.iconbitmap(r"C:/Users/Juliao JM/Downloads/py-white.ico")
master.title("Button Widget")
master.geometry("600x400")

def func_here():
	print("Button is pressed!")

b1 = Button(master, text="OK", command=func_here)
b1.pack()

master.mainloop()