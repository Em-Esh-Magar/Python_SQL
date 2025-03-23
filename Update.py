import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "@M.S._Magar7",
    database = "Python_Sql"
)

cursor = mydb.cursor()

query = "Update Students set address = 'Kathmandu' where address = 'KTM' "


cursor.execute(query)

mydb.commit()