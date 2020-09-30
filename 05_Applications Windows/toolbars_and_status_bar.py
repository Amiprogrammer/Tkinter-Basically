from tkinter import *

root = Tk()
root.iconbitmap(r"C:\Users\Juliao JM\Downloads\py-white.ico")
root.title("First Program")
root.geometry("600x400")

toolbars = Frame(root)
toolbars.pack(side=TOP, fill=X)

b1 = Button(toolbars, text="OPEN")
b1.pack(side=LEFT, padx=4)

b2 = Button(toolbars, text="CLOSE")
b2.pack(side=LEFT, padx=4)

status_bar = Frame(root)
status_bar.pack(side=BOTTOM, fill=X)

copy = Label(status_bar, text="copyright 2020. built by Juliao-Martins")
copy.pack()

root.mainloop()