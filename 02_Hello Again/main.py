from tkinter import *

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



root = Tk()
root.title("First Program")

# object 
app = App(master=root)

root.mainloop()