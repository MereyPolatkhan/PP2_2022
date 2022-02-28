# 1. Create a generator that generates the squares of numbers up to some number N.

n = int(input()) 

def square(x):
    for i in range(1, x + 1): 
        yield i * i 

a = list(square(n))
print(a)

# 5
# [1, 4, 9, 16, 25]