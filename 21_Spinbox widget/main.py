from tkinter import *

master = Tk()

# spin = Spinbox(master, from_=0, to=5, variable=var)
# spin.pack()

spin = Spinbox(master, value=(7,17,2001,1980))
spin.pack()

master.mainloop()