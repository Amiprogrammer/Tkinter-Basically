from tkinter import *
from tkinter import messagebox

root = Tk()
root.iconbitmap(r"C:\Users\Juliao JM\Downloads\py-white.ico")
root.title("First Program")
root.geometry("600x400")

def cursor_in(event):
	m_in_status.config(text="IN", fg="green")

def cursor_out(event):
	m_in_status.config(text="OUT", fg="red")

def keyboard_capture(event):
	k_in_status.config(text=f"{repr(event.keysym)}", fg="lightskyblue")

	# end the program with End arrow
	if( event.keysym == "End" ):

		if( messagebox.askyesno("First Program","do you want to end the program!") ):
			root.destroy()
		else:
			messagebox.showinfo("First Program","it's canceled!")


index = Label(root, text="Application Detection", font=("Cooper Black",20), bg="black", fg="white")
index.pack()

form_frame = Frame(root, bg="black")
form_frame.pack(pady=50)

m_in = Label(form_frame, text="Cursor Status :", bg="black", fg="white", font=("Courier New",14))
m_in.grid(row=0, column=0, columnspan=1, pady=3, padx=15)

m_in_status = Label(form_frame, text="", bg="black", fg="white", font=("Courier",14))
m_in_status.grid(row=0, column=1, columnspan=1)

k_in = Label(form_frame, text="Keyboard Status :", bg="black", fg="white", font=("Courier New",14))
k_in.grid(row=1, column=0, columnspan=1, pady=3, padx=15)

k_in_status = Label(form_frame, text="", bg="black", fg="white", font=("Courier",14))
k_in_status.grid(row=1, column=1, columnspan=1)

close_status = Label(root, text="press the \"End\" arrow to cloose this program!", bg="black", fg="white", font=("Times New Roman Italic",13))
close_status.pack()

root.bind("<Enter>", cursor_in)
root.bind("<Leave>", cursor_out)
root.bind("<Key>", keyboard_capture)

root.config(bg="black")
root.mainloop()