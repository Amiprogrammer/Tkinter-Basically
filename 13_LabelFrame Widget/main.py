from tkinter import *

master = Tk()
master.iconbitmap(r"C:/Users/Juliao JM/Downloads/py-white.ico")
master.title("LabelFrame Widget")
master.geometry("600x400")

name_index = LabelFrame(master,  text="Name", padx=10, pady=10)
name_index.pack(padx=4, pady=4)

name_entry = Entry(name_index)
name_entry.pack()

master.mainloop()