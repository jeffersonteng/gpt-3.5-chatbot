import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (content) VALUES (?)",
            ('First Query',)
            )
cur.execute("INSERT INTO posts (content) VALUES (?)",
            ('Second Query',)
            )

connection.commit()
connection.close()