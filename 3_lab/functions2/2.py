from movie import movies 

def higher5_5(mov):
    a = []
    for movie in mov:
        if movie["imdb"] >= 5.5:
            a.append(movie["name"])
    return a

print(higher5_5(movies))