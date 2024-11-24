import random
from imdb import IMDb

ia = IMDb()

def fetch_movies_by_genre(genre, count=5):
    """
    Fetches a list of movies based on genre using IMDbPY.

    Parameters:
    genre (str): Genre to fetch movies for (e.g., "Action", "Comedy").
    count (int): Number of movies to fetch.

    Returns:
    list: List of movie titles.
    """
    movies = []
    try:
        results = ia.search_movie(genre)
        for movie in results[:count]:
            movies.append(movie['title'])
    except Exception as e:
        print(f"Error fetching movies for genre '{genre}': {e}")
    return movies

genres = ["Action", "Adventure", "Animated", "Comedy", "Drama", "Fantasy", "Historical", "Horror", "Musical", "Noir",
          "Romance", "Science fiction", "Thriller", "Western"]

movies = {}
for genre in genres:
    print(f"Fetching movies for genre: {genre}...")
    movies[genre] = fetch_movies_by_genre(genre)
    print(f"Found {len(movies[genre])} movies for {genre}.")

# Function to recommend a movie based on genre
def recommend_movie(genre):
    """
    Recommends a movie from the specified genre.

    Parameters:
    genre (str): Genre to recommend a movie from.

    Returns:
    str: Recommended movie title.
    """
    if genre in movies and movies[genre]:
        return random.choice(movies[genre])
    else:
        return "Sorry, no movies found for that genre."

print("\nAvailable genres:", ", ".join(genres))
user_input = input("Enter your preferred genre: ").capitalize()
print("We recommend:", recommend_movie(user_input))
