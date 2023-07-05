import mysql.connector

mydb = mysql.connector.connect 
(
    host="localhost",
    username="root",
    password=""
    database="DatabaseSummative"

)

mycursor = mydb.cursor()

mycursor.execute("create database summativeDB")
print("Database created")


