from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	username="root",
	password="jmq123jj",
	database="tkinter"
)

print(mydb)