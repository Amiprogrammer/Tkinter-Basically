from tkinter import *
import mysql.connector

db = mysql.connector.connect(
	host="localhost",
	username="root",
	password="jmq123jj"
)

mycursor = db.cursor()

# mycursor.execute("CREATE DATABASE tkinter")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
	print(x)