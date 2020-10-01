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

for x in result:
	print(x)