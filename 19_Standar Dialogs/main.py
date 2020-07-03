from tkinter import *
from tkinter import messagebox

master = Tk()
master.title("messagebox")

# messagebox.showinfo("learn msg","Hello, World!")
# messagebox.showwarning("learn msg","Hello, World!")
# messagebox.showerror("learn msg","Hello, World!")
# messagebox.askquestion("learn msg","Hello, World!")
# messagebox.askokcancel("learn msg","Hello, World!")
messagebox.askretrycancel("learn msg","Hello, World!")

master.mainloop()