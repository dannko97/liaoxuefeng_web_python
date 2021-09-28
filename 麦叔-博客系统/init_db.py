import sqlite3

conn = sqlite3.connect('database.db')

with open('db.sql') as f:
    conn.executescript(f.read())

cur = conn.cursor()
cur.execute("INSERT INTO posts (title, content) VALUE (?, ?)", ('学习Flask1', '跟着麦叔学习flask第一部分'))

conn.commit()
conn.close()