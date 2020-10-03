from tkinter import *

master = Tk()
master.iconbitmap(r"C:/Users/Juliao JM/Downloads/py-white.ico")
master.title("Popup Menu")
master.geometry("600x400")

number = 0

def clicked():
	global number
	number += 1
	filemenu.entryconfig(0, label=str(number))

menubar = Menu(master)

filemenu = Menu(menubar, tearoff=0, postcommand=clicked)
menubar.add_cascade(label="file", menu=filemenu)
filemenu.add_command(label=str(number))
filemenu.add_command(label="exit", command=master.destroy)

master.config(menu=menubar)

master.mainloop()