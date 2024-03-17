import sqlite3

con = sqlite3.connect('base.db')
cursor = con.cursor()

sql = """ 
CREATE TABLE produtos (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    marca TEXT NOT NULL,
                    variacao TEXT NOT NULL)
"""

cursor.execute(sql)
con.commit()

cursor.close()
con.close() #finaliza conexão