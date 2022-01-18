import sqlite3

connection = sqlite3.connect("films.sqlite")
cursor = connection.cursor()
result = cursor.execute(""" SELECT title FROM filmsWHERE title LIKE "%Астерикс%" AND title NOT LIKE "%Обеликс%" """).fetchall()
for i in result:
    print(i[0])
