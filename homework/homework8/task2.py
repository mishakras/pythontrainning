import sqlite3
conn = sqlite3.connect('example.sqlite')
cursor = conn.cursor()
cursor.execute('SELECT * from presidents')
data = cursor.fetchall()
