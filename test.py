def factorial(n):
    k = 1
    for i in range(1, n + 1):
        k = k * i
    return k  

def combination(all, a):
    res = float(factorial(all)) / float((factorial(a) * factorial(all-a))) 
    return res



first = combination(3, 2) * 0.5 * 0.5 * 0.5 + combination(3,3) * (0.5 ** 3)
print(first)

second = combination(2, 1) * (0.5 ** 2) + combination(2, 0) * (0.5 ** 2)
print(second)

print(combination(10, 3) * (0.4 ** 3) * (0.6 ** 7))