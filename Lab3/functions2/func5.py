def compute_category_imdb(movie_list, category):
    counter = 0
    total = 0

    for movie in movie_list:
        if movie["category"] == category:
            counter += 1
            total += movie["imdb"]

    return total / counter