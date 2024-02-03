def compute_avg_imdb(movie_list):
    counter = 0
    total = 0

    for movie in movie_list:
        counter += 1

        total += movie["imdb"]

    return total / counter