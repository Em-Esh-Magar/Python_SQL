import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "@M.S._Magar7",
    database = "Python_Sql"
)

cursor = mydb.cursor()

query = "Insert into Students (name,age,address) values(%s,%s,%s)"
value = [("Ram",23,"Goldhunga"),
         ("Raju",22,"KTM"),
         ("Hari",34,"Pokhara"),
         ("Shyam",33,"KTM")
        ]

cursor.executemany(query,value)

mydb.commit()