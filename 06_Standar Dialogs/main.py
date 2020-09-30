from tkinter import *
from tkinter import messagebox

root = Tk()
root.iconbitmap(r"C:\Users\Juliao JM\Downloads\py-white.ico")
root.title("First Program")
root.geometry("600x400")

"""
# That is show all messagebox
# show info message boxes
messagebox.showinfo("info","Hello, World!")
# show warning message boxes
messagebox.showwarning("warning","Hello, World!")
# show error message boxes
messagebox.showerror("error","Hello, ErrorX")
"""

# That is decision in messagebox
# if( n:= messagebox.askquestion("question","do you want to continue...") ):
# if( n:= messagebox.askyesno("yesno","do you want to continue...")):
# ( n:= messagebox.askokcancel("okcancel","are you sure!")):
if( n:= messagebox.askretrycancel("retrycancel","do yo want to stay the program!")):
	print(f"user chose {n}")
	messagebox.showinfo("info","the program will be continue...")
else:
	print(f"user chose {n}")
	messagebox.showwarning("warning","the program will be close!")
	root.destroy()

root.mainloop()