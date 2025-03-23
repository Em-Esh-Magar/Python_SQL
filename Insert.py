import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "@M.S._Magar7",
    database = "Python_Sql"
)

cursor = mydb.cursor()

query = "Insert into Students (name,age,address) values(%s,%s,%s)"
value = ("Em Esh",23,"Goldhunga")

cursor.execute(query,value)

mydb.commit()