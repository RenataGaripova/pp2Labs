def make_sublist(movie_list):
    result = []

    for movie in movie_list:
        if movie["imdb"] > 5.5:
            result.append(movie)

    return result
