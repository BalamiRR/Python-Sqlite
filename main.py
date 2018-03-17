import sqlite3

con = sqlite3.connect("Database.db")

cursor = con.cursor()

def createTable():
    cursor.execute("CREATE TABLE Students (name TEXT,surName TEXT,number INT,grades INT)")
    con.cursor()
    con.close()

def addValue():
#seçili veritabanına veri ekliyoruz.
    cursor.execute("INSERT INTO Students VALUES('Mustafa Kemal','Ataturk','1','5.0')")
    con.commit()
    con.close()


addValue()
