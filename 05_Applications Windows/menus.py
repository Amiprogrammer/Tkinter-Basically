from tkinter import *

root = Tk()
root.iconbitmap(r"C:\Users\Juliao JM\Downloads\py-white.ico")
root.title("first program")
root.geometry("600x400")

def func_here():
	print("OK!")

# pulldown menu
menubar = Menu(root)

menubar.add_command(label="open", command=func_here)
menubar.add_command(label="exit", command=root.destroy)

# to display the menu
root.config(menu=menubar)

root.mainloop()