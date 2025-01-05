#pip install IMDbPY        // nem imdb, mert nem fogja meg találni //


from imdb import IMDb

ia = IMDb()
movie_name = input("Enter the movie name: ")
movies = ia.search_movie(movie_name)

if movies:
    movie = movies[0]
    ia.update(movie)
    directors = movie.get('directors')
    if directors:
        print("Director(s):")
        for director in directors:
            print(director['name'])
    else:
        print("No director information found.")
else:
    print("Movie not found.")