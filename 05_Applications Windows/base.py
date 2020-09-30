from tkinter import *

root = Tk()
root.iconbitmap(r"C:\Users\Juliao JM\Downloads\py-white.ico")
root.title("Firs Program")
root.geometry("600x400")

top = Toplevel()

x1 = Message(top, text="this is program built by tkinter!")
x1.pack()

b = Button(top, text="DISMISS", bg="red", fg="white", command=top.destroy)
b.pack()


root.mainloop()