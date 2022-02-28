# Define a function with a generator which can iterate 
# the numbers, which are divisible by 3 and 4, 
# between a given range 0 and n.

n = int(input()) 

def div(x):
    for i in range(x):
        if i % 12 == 0:
            yield i 

a = list(div(n)) 

print(a)

# 100
# [0, 12, 24, 36, 48, 60, 72, 84, 96]