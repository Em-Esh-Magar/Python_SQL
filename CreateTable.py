import mysql.connector

mydb1 = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "@M.S._Magar7",
    database = "Python_Sql"
)

my_cursor = mydb1.cursor()

my_cursor.execute("Create Table Students (name Varchar(20), age int, address varchar(30))")
