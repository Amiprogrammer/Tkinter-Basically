from tkinter import *

master = Tk()
master.iconbitmap(r"C:/Users/Juliao JM/Downloads/py-white.ico")
master.title("Listbox Widget")
master.geometry("600x400")

listbox = Listbox(master)
listbox.pack()

listbox.delete(0, END)
listbox.insert(0, "a default")

for i in ["nana","nene","nini","nono","nunu"]:
	listbox.insert(END, i)


master.mainloop()