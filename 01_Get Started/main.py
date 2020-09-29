"""
authors : Juliao Martins

you want to used the tkinter module, needed the importing module, then:

import tkinter
import tkinter as tk
	or
from tkinter import *

depending your code!

"""

from tkinter import *

root = Tk()
root.title("Fist Window") # this method to change the window tilte
root.geometry("400x200") # to change the size of window

x = Label(root, text="Hello, World!", font=("Times New Roman",17))
x.pack()

root.mainloop()