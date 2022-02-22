def factorial(n):
    k = 1
    for i in range(1, n + 1):
        k = k * i
    return k  

def combination(all, a):
    res = float(factorial(all)) / float((factorial(a) * factorial(all-a))) 
    return res

res = 0.6 * 0.4 * 0.4  * 3

print(round(res, 4))