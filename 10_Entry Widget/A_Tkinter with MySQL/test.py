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
master.geometry("600x400")

Label(master, text="Estudent Table").pack()

form_estudent1 = Frame(master)
form_estudent1.pack()
form_estudent2 = Frame(master)
form_estudent2.pack()

number_est = Label(form_estudent1, text="N0")
number_est.grid(row=0, column=0)

name_est = Label(form_estudent1, text="Name")
name_est.grid(row=0, column=1)

gender_est = Label(form_estudent1, text="Gender")
gender_est.grid(row=0, column=2)

address_est = Label(form_estudent1, text="Address")
address_est.grid(row=0, column=3)

for i,x in enumerate(result):
	
	Label(form_estudent2, text=f"{x[0]}").grid(row=i, column=0)

	Label(form_estudent2, text=f"{x[1]}").grid(row=i, column=1)

	Label(form_estudent2, text=f"{x[2]}").grid(row=i, column=2)

	Label(form_estudent2, text=f"{x[3]}").grid(row=i, column=3)


master.mainloop()