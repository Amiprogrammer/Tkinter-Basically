from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	username="root",
	password="jmq123jj",
	database="tkinter"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM estudent")
result = mycursor.fetchall()

master = Tk()
master.iconbitmap(r"C:/Users/Juliao JM/Downloads/py-white.ico")
master.title("firs program")
master.geometry("650x450")

def input_date():
	pass

def canceled():
	entry_name.delete(0, END)
	entry_address.delete(0, END)

indexing = Label(master, text="Estudent Table", font=("Courier New",26))
indexing.pack(pady=20)

form_estudent1 = Frame(master)
form_estudent1.pack()
form_estudent2 = Frame(master)
form_estudent2.pack()

number_est = Label(form_estudent1, text="N0", font=("Cooper Black",11))
number_est.grid(row=0, column=0, padx=25)

name_est = Label(form_estudent1, text="Name", font=("Cooper Black",11))
name_est.grid(row=0, column=1, padx=25)

gender_est = Label(form_estudent1, text="Gender", font=("Cooper Black",11))
gender_est.grid(row=0, column=2, padx=25)

address_est = Label(form_estudent1, text="Address", font=("Cooper Black",11))
address_est.grid(row=0, column=3, padx=25)

for i,x in enumerate(result):
	
	number = Label(form_estudent2, text=f"{x[0]}")
	number.grid(row=i, column=0, padx=28)

	name = Label(form_estudent2, text=f"{x[1]}".capitalize())
	name.grid(row=i, column=1, padx=28)

	gender = Label(form_estudent2, text=f"{x[2]}".upper())
	gender.grid(row=i, column=2, padx=28)

	address = Label(form_estudent2, text=f"{x[3]}".capitalize())
	address.grid(row=i, column=3, padx=28)


inserting = Label(master, text="Insert New Date", font=("Courier New",22))
inserting.pack(pady=30)

form_insert = Frame(master)
form_insert.pack()

label_name = Label(form_insert, text="name:")
label_name.grid(row=0, column=0)

entry_name = Entry(form_insert)
entry_name.grid(row=0, column=1, padx=18)

label_gender = Label(form_insert, text="Gender")
label_gender.grid(row=1, column=0)

var = StringVar()
var.set(None)

masculin = Radiobutton(form_insert, text="M", variable=var, value="m")
femenin = Radiobutton(form_insert, text="F", variable=var, value="f")

masculin.grid(row=1, column=1)
femenin.grid(row=1, column=2)

label_address = Label(form_insert, text="Address:")
label_address.grid(row=2, column=0)

entry_address = Entry(form_insert)
entry_address.grid(row=2, column=1, padx=18)

input_button = Button(form_insert, text="OK", bg="blue", fg="white", command=input_date)
input_button.grid(row=3, columnspan=3, pady=20)

cancel_button = Button(form_insert, text="Cancel", bg="red", fg="white", command=canceled)
cancel_button.grid(row=4, columnspan=3)

master.mainloop()