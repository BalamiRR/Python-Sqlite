import sqlite3

con = sqlite3.connect("Database.db")

cursor = con.cursor()

def createTable():
    cursor.execute("CREATE TABLE Students (name TEXT,surName TEXT,number INT,grades INT)")
    con.cursor()
    con.close()

def addValue():
    cursor.execute("INSERT INTO Students VALUES('Mustafa','Ataturk',55,5.0)")
    con.commit()
    con.close()


createTable()
addValue()
