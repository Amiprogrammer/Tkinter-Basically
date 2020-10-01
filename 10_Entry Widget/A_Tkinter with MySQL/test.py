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

for x in result:
	Label(master, text=f"{x}").pack()


master.mainloop()