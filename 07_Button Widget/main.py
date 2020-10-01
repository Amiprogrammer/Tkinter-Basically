from tkinter import *

master = Tk()
master.iconbitmap(r"C:/Users/Juliao JM/Downloads/py-white.ico")
master.title("Button Widget")
master.geometry("600x400")

def func_here():
	print("Button is pressed!")

image = PhotoImage(file="github.png")

b1 = Button(master, text="OK", command=func_here, state=NORMAL, image=image, compound=CENTER, fg="blue")
b1.pack(padx=40, pady=40)

master.mainloop()