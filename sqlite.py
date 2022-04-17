import sqlite3
import json
from pathlib import Path
#sends data to the database 
# movies = json.loads(Path("movies.json").read_text())
# #print(movies)

# with sqlite3.connect("db.sqlite3") as conn:
#     command = "INSERT INTO Movies VALUES(?,?,?)"

#     for movie in movies:
#         conn.execute(command, tuple(movie.values()))

#     conn.commit()

#retrieving data from the database
with sqlite3.connect("db.sqlite3") as conn:
    command = " SELECT * FROM Movies"
    cursor = conn.execute(command)

    movies =cursor.fetchall()
    print(movies)

    # for row in cursor:
    #     print(row )

    

