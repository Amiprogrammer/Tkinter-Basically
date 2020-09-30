from tkinter import *

root = Tk()
root.title("First Program")
root.geometry("400x200")

x = Label(root, text="Widget Configuration")
x.pack()

x.config(pady=10)
x.config(fg="blue")
x.config(font=("Fira Code Medium",17))
x.config(bg="black", fg="white")
x.config(pady=15)

root.mainloop()