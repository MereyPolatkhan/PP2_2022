a = int(input()) 
b = int(input()) 

def squares(x, y):
    for i in range(x, y + 1):
        yield i ** 2

arr = list(squares(a, b)) 

for i in arr:
    print(i, end=' ')

# 1 
# 5
# 1 4 9 16 25 