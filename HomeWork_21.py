import sqlite3

connection = sqlite3.connect("music_db (1).sqlite")
cursor = connection.cursor()
result1 = cursor.execute(f"""SELECT(GenreId) FROM Genre WHERE Name="Rock" """).fetchone()
result2 = cursor.execute(f"""SELECT(TrackId) FROM Track WHERE GenreId = {int(result1[0])}""").fetchall()
lst = []
for i in result2:
    result3 = cursor.execute(f"""SELECT (AlbumId) FROM Track WHERE TrackId = {int(i[0])}""").fetchall()
    lst.append(result3[0])
lst = list(set(lst))
for i in lst:
    result4 = cursor.execute(f"""SELECT Title FROM Album WHERE AlbumId = {int(i[0])} """).fetchall()
    print(result4[0][0])
