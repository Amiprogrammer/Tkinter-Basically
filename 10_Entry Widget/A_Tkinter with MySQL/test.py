from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	username="root",
	password="jmq123jj",
	database="tkinter"
)

mycursor = mydb.cursor()

sql = "INSERT INTO estudent (name,gender,address) VALUES (%s,%s,%s)"
val = [
	("joao nunes","m","becora"),
	("elia amaral","f","fatumeta"),
	("aurito valentiin","m","cacaulidu")
]

mycursor.executemany(sql,val)

mydb.commit()

print(mycursor.rowcount, " inserted record(s).")