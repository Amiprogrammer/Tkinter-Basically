from tkinter import *

master = Tk()
master.title("scrollbar")

scrollbar = Scrollbar(master)
scrollbar.pack(fill=Y, side=RIGHT)


list = Listbox(master, yscrollcommand=scrollbar.set)

for i in range(1,2000):
	list.insert(END, i)


list.pack()

scrollbar.config(command=list.yview)

master.mainloop()