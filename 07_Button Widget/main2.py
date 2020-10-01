from tkinter import *

master = Tk()
master.iconbitmap(r"C:\Users\Juliao JM\Downloads\py-white.ico")
master.title("Button Widget")
master.geometry("600x400")

f = Frame(master, width=32, height=32)
f.pack(fill=BOTH, expand=1)
f.pack_propagate(0)

Button(f, text="Quit", command=master.destroy, state=DISABLED, bg="red", fg="black", font=("Courier New",14)).pack()

master.mainloop()