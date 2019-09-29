from media import Movie
import fresh_tomatoes as ft
from mov_dict import d

def main():
    movies = []
    for title, urls in d.items():
        poster = urls[0]
        trailer = urls[1]
        movies.append(Movie(title, poster, trailer))

    ft.open_movies_page(movies)

if __name__ == '__main__':
    main()
