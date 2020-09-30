from tkinter import *

root = Tk()
root.iconbitmap(r"C:\Users\Juliao JM\Downloads\py-white.ico")
root.title("First Program")
root.geometry("600x400")

def clicked(event):
	pass

root.bind("<Button-1>", clicked)

root.mainloop()