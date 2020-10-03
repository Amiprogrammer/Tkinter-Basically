from tkinter import *
	
master = Tk()
master.iconbitmap(r"C:/Users/Juliao JM/Downloads/py-white.ico")
master.title("Toplevel Menu")
master.geometry("600x400")

def ok():
	print("OK!")

# initialize with Menu class
menubar = Menu(master)

menubar.add_command(label="file", command=ok)
menubar.add_command(label="edit", command=ok)
menubar.add_command(label="help", command=ok)
menubar.add_command(label="exit", command=master.destroy)

# to show the menu
master.config(menu=menubar)

master.mainloop()