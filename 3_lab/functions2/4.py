from movie import movies

def average_imdb(mov):
    sum = 0
    for movie in mov:
        sum += movie["imdb"]
    return sum / len(mov)

print(average_imdb(movies))
