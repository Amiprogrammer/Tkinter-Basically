from tkinter import *
from tkinter import messagebox
import random

# template
class App(Frame):

	def __init__(self,master=None):
		super().__init__(master)
		self.pack()
		self.master.geometry("800x600")
		# call the method
		self.all_here()

	def all_here(self):

		self.status = Label(self)
		self.status["text"] = "Hello, World!"
		self.status["font"] = ("Courier New",28)
		self.status.pack(pady=150)

		self.button_frame = Frame(self)
		self.button_frame.pack()

		self.b1 = Button(self.button_frame)
		self.b1["text"] = "clik here"
		self.b1["bg"] = "green"
		self.b1["fg"] = "white"
		self.b1["command"] = self.manipulate
		self.b1.grid(row=0, column=0, padx=6)

		self.b2 = Button(self.button_frame)
		self.b2["text"] = "cancel"
		self.b2["bg"] = "red"
		self.b2["fg"] = "white"
		self.b2["command"] = self.reset
		self.b2.grid(row=0, column=1, padx=6)

	def manipulate(self):
		pass

	def reset(self):
		pass


root = Tk()
root.title("First Program")

# object 
app = App(master=root)

root.mainloop()