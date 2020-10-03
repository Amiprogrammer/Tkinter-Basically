from tkinter import *

master = Tk()
master.iconbitmap(r"C:/Users/Juliao JM/Downloads/py-white.ico")
master.title("Pulldown Menu")
master.geometry("600x400")

def ok():
	print("OK!")

menubar = Menu(master)

# create menu instance
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="file", menu=filemenu) # to add menu instance
filemenu.add_command(label="open", command=ok)
filemenu.add_command(label="save", command=ok)
filemenu.add_command(label="save as", command=ok)
filemenu.add_separator() # to add separator
filemenu.add_command(label="exit", command=master.destroy)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="edit", menu=editmenu)
editmenu.add_command(label="copy", command=ok)
editmenu.add_command(label="cut", command=ok)
editmenu.add_command(label="paste", command=ok)

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="help", menu=helpmenu)
helpmenu.add_command(label="about", command=ok)

# to show the menu
master.config(menu=menubar)

master.mainloop()