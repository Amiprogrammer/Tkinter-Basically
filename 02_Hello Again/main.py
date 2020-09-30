from tkinter import *

# template
class App(Frame):

	def __init__(self,master=None):
		super().__init__(master)
		self.pack()


root = Tk()
root.title("First Program")

# object 
app = App(master=root)

root.mainloop()