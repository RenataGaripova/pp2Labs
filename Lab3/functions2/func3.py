def give_certain_movies(movie_list, category):
    result = []

    for movie in movie_list:
        if movie["category"] == category:
            result.append(movie)

    return result
