from media import Movie
import fresh_tomatoes as ft

def main():
    movies = []
    movies.append(Movie("Interstellar", "https://m.media-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg",
    "https://www.youtube.com/watch?v=zSWdZVtXT7E"))

    movies.append(Movie("Inception", "https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=d3A3-zSOBT4"))

    movies.append(Movie("Batman: The Dark Knight Rises", "https://www.movienewsletters.net/photos/117274R1.jpg",
    "https://www.youtube.com/watch?v=g8evyE9TuYk"))
    ft.open_movies_page(movies)

if __name__ == '__main__':
    main()
