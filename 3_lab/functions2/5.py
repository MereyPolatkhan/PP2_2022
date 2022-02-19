from movie import movies

def average_of_category(s):
    sum = 0
    k = 0
    for movie in movies:
        if movie["category"] == s:
            k += 1
            sum += movie["imdb"]
    return sum/k

print(average_of_category("Romance"))