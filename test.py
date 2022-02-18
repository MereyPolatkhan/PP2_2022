arr = []
n = int(input())
for i in range(n): 
    d = dict() 
    name = input() 
    imdb = int(input())
    category = input() 
    d = {"name": name, "imdb": imdb, "category": category}
    arr.append(d)

for i in arr:
    print(i)
