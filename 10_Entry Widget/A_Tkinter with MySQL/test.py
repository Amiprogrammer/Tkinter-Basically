from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	username="root",
	password="jmq123jj",
	database="tkinter"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE estudent (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), gender CHAR(1), address VARCHAR(255))")

mycursor.execute("SHOW TABLES")

for x in mycursor:
	print(x)