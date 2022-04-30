import sqlite3

conn = sqlite3.connect('table.db')
cur = conn.cursor()
cur.execute("SELECT * FROM society")
one_result = cur.fetchone()

print(one_result[0])
print(one_result[1])
print(one_result[2])
print(one_result[3])
print(one_result[4])