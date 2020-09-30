from tkinter import *

root = Tk()
root.iconbitmap(r"C:\Users\Juliao JM\Downloads\py-white.ico")
root.title("first program")
root.geometry("600x400")

def func_here():
	print("OK!")

"""
# toplevel menu
menubar = Menu(root)

menubar.add_command(label="open", command=func_here)
menubar.add_command(label="exit", command=root.destroy)

# to display the menu
root.config(menu=menubar)
"""

# this is pulldown menu
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="file", menu=filemenu)
filemenu.add_command(label="open", command=func_here)
filemenu.add_command(label="save", command=func_here)
filemenu.add_command(label="save as", command=func_here)
filemenu.add_separator()
filemenu.add_command(label="exit", command=root.destroy)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="edit", menu=editmenu)
editmenu.add_command(label="copy", command=func_here)
editmenu.add_command(label="cut", command=func_here)
editmenu.add_separator()
editmenu.add_command(label="paste", command=func_here)

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="help", menu=helpmenu)
helpmenu.add_command(label="about", command=func_here)

# display menu
root.config(menu=menubar)

root.mainloop()