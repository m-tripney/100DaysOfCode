from collections import Counter
from collections import defaultdict
from collections import namedtuple
from urllib.request import urlretrieve
import csv

movie_data_source = "https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv"
movie_data_csv = "movie_data.csv"

# Retrieve content from movie_data and put it in movie_data.csv
urlretrieve(movie_data_source, movie_data_csv)

# Every movie is going to be stored in a namedtuple called 'Movie'
Movie = namedtuple("Movie", "title year score")


def filter_movies_by_director(data=movie_data_csv):
    directors = defaultdict(list)
    with open(data) as f:
        for line in csv.DictReader(f):
            try:
                director = line["director_name"]
                movie = line["movie_title"].replace("\xa0", "")
                year = int(line["title_year"])
                score = float(line["imdb_score"])
            except ValueError:
                continue

            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)

        return directors


directors = filter_movies_by_director(movie_data_csv)

cnt = Counter()
for director, movies in directors.items():
    cnt[director] += len(movies)
    for movie in movies:
        print(f"'{movie.title}' by {director} ({movie.year}) scores {movie.score}")

print(cnt.most_common(5))  # most_common() returns a list
print(sorted(set(cnt.elements())))
for item in cnt.most_common(5):
    print(f"{item[0]} has {item[1]} films listed")
