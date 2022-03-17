a = [int(x) for x in input().split()] 

def multiply(a):
    k = 1
    for i in a:
        k *= i 
    return k

print(multiply(a))