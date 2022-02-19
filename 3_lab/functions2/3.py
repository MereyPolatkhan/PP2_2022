from movie import movies 

def category(categ):
    a = []
    for movie in movies:
        if movie["category"] == categ:
            a.append(movie["name"])
    return a

print(category("Thriller"))