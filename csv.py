import json 
from pathlib import Path
# creating json data 
# movies = [
#     {"id":1, "title":"terminater","year":1970},
#     { "id":2, "title":"Squid Game" , "year": 2020}
# ]

# data = json.dumps(movies)
# Path("movies.json").write_text(data)

#working with json data
data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies[1]["title"])