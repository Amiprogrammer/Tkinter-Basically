from tkinter import *
from random import choice

root = Tk()
root.title("First Program")
root.geometry("400x200")

x = Label(root, text="Widget Configuration")
x.pack()

# x.config(pady=10)
# x.config(fg="blue")
# x.config(font=("Fira Code Medium",17))
# x.config(bg="black", fg="white")
x.config(pady=15)
# x["bg"] = "white" or x.config(bg="white")
x["fg"] = "black"
x["font"] = ("Courier New",20)

def here():
	bg = choice(["red","yellow","purple","orange","green","pink","chocolate","lightblue"])
	x.config(text=bg, bg=bg)
	root.config(bg=bg)

b = Button(root, text="change bg", command=here)
b.pack()

b.config(bg="black", fg="white", font=("Cooper Black",11))

root.mainloop()