from tkinter import *

master = Tk()
master.iconbitmap("C:/Users/Juliao JM/Downloads/py-white.ico")
master.title("Entry Widget")
master.geometry("600x400")

"""
e = Entry(master)
e.pack(pady=20)

e.delete(0, END)
e.insert(0, "a default value!")
e.delete(0, END)
"""

def get_in_input():
	entry.focus_set()
	x = entry.get()
	if( len(x) > 1):
		result.config(text=f"User typed {x}.")
		print(f"User Typed {x}.")
		entry.delete(0, END)
	else:
		print("None")

def delete_all_input():
	entry.delete(0, END)
	result.config(text="Result")

form = Frame(master)
form.pack(pady=40)

label = Label(form, text="Type Something :", font=("Courier New",12))
label.grid(row=0, column=0)

entry = Entry(form, font=("Courier New",12))
entry.grid(row=0, column=1)

confirm_button = Button(form, text="OK", font=("Courier New",12), bg="black", fg="white", command=get_in_input)
confirm_button.grid(row=1, column=0, pady=10)

deleted_button = Button(form, text="Delete", font=("Courier New",12), bg="red", fg="white", command=delete_all_input)
deleted_button.grid(row=1, column=1)

result = Label(form, text="Result", font=("Courier New",15))
result.grid(row=2, columnspan=2, pady=60)

master.mainloop()