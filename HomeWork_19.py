import sqlite3

connection = sqlite3.connect("films.sqlite")
cursor = connection.cursor()
result = cursor.execute(""" SELECT title FROM films WHERE genre = 1 AND year BETWEEN 1995 AND 2000""").fetchall()
for i in result:
    print(i[0])
