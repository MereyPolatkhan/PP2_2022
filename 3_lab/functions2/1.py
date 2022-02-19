from movie import movies

def isHigher5_5(n):
    if movies[n]["imdb"] >= 5.5:
        return True
    else:
        return False

            
      
n = int(input()) 

print(isHigher5_5(n))
