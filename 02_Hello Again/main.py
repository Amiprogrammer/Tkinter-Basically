from tkinter import *

# template
class App(Frame):

	def __init__(self,master=None):
		super().__init__(master)
		self.pack()
		# call the method
		self.all_here()

	def all_here(self):
		pass


root = Tk()
root.title("First Program")

# object 
app = App(master=root)

root.mainloop()