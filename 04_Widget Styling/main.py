from tkinter import *

root = Tk()
root.iconbitmap(r"C:\Users\Juliao JM\Downloads\py-white.ico")
root.title("First Program")
root.geometry("600x400")

def clicked(event):
	print(f"position : x  {repr(event.x_root)} y  {repr(event.y_root)}")

def keyboard(event):
	print(f"keyboard :  {repr(event.keysym)}")

root.bind("<ButtonRelease-1>", clicked)
root.bind("<Key>", keyboard)

root.mainloop()