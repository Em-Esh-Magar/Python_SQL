import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "@M.S._Magar7",
    database = "Python_Sql"
)

cursor = mydb.cursor()

query = "Delete from Students where name = 'Em Esh' "

cursor.execute(query)

mydb.commit()