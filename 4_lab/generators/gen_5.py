n = int(input()) 

def gen(x):
    for i in range(x, -1, -1):
        yield i 

a = list(gen(n))
print(a)

# 10
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]