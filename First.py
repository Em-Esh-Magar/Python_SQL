import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "@M.S._Magar7"
)

cursor = mydb.cursor()

cursor.execute("Show Databases")

for x in cursor:
    print(x)