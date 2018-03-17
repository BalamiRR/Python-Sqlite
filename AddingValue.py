import sqlite3 as sql
import random as rd
import time
import datetime


con = sql.connect("Time.db")
cursor = con.cursor()

def createTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS Tablo1 (times REAL,date TEXT,key TEXT,value REAL)")

def addrandomly():
    times = time.time()
    date = str(datetime.datetime.fromtimestamp(times).strftime("%Y-%M-%D   %H-%M-%S"))
    key = "Python Sqlite"
    value = rd.randrange(0,10)
    cursor.execute("INSERT INTO Tablo1 (times,date,key,value) VALUES(?,?,?,?)",(times,date,key,value))
    con.commit()

createTable()

i=0
while(i<10):
    addrandomly()
    time.sleep(1)
    i+=1

con.close()
