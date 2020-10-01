from tkinter import *
import mysql.connector

db = mysql.connector.connect(
	host="localhost",
	username="root",
	password="jmq123jj"
)

print(db)