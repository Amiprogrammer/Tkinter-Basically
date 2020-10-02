from tkinter import *

master = Tk()
master.iconbitmap(r"C:/Users/Juliao JM/Downloads/py-white.ico")
master.title("Label Widget")
master.geometry("800x600")

label1 = Label(master, text="Hello, World!")
label1.pack()

var = StringVar()
var.set("Hello, Juliao Martins!")

label2 = Label(master, textvariable=var)
label2.pack()

label3 = Label(master, text="python is interpreter languague!".title())
label3.pack()

label4 = Label(master, text="Cooper Black Font", font=("Cooper Black",12))
label4.pack()

label5 = Label(master, text="Courier New Font", font=("Courier New",46))
label5.pack()

photo = PhotoImage(file=r"C:/Users/Juliao JM/Downloads/py-white.png")

label6 = Label(master, text="Python", image=photo, bg="blue", fg="yellow", font=("Cooper Black",44), compound=CENTER)
label6.photo = photo
label6.pack()

master.mainloop()