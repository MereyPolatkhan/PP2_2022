import math

a = [int(x) for x in input().split()] 

def multiply(a):
    return math.prod(a)

print(multiply(a))