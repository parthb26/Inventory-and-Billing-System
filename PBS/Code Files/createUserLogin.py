import sqlite3

conn = sqlite3.connect("user_credentials.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)")
cursor.execute("INSERT INTO USER VALUES('Admin','Adm_8420')")

conn.commit()
conn.close()
