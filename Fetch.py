import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "@M.S._Magar7",
    database = "Python_Sql"
)

cursor = mydb.cursor()

query = "Select * From Students"

cursor.execute(query)

for x in cursor:
    print(x)