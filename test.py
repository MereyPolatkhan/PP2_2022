# import math

# def factorial(n):
#     k = 1
#     for i in range(1, n + 1):
#         k = k * i
#     return k  

# def combination(all, a):
#     res = float(factorial(all)) / float((factorial(a) * factorial(all-a))) 
#     return res


# def bernoulli(k, n, p, q):
#     return combination(n, k) * (p ** k) * (q ** (n-k))


# def local_laplace():
#     k = int(input("k: ")) 
#     n = int(input("n: ")) 
#     p = float(input("p: ")) 
#     q = 1 - p
    
#     npq = (math.sqrt(n * p * q))

#     print(f'Pn(k)= {1/npq} fi(x)')
#     print(f'x= {(k - n * p)/npq}')


# def integral_laplace():
#     k1 = int(input("k1: "))
#     k2 = int(input("k2: ")) 
#     n = int(input("n: ")) 
#     p = float(input("p: ")) 
#     q = 1 - p

#     snpq = math.sqrt(n*p*q)

#     print(f'x1= {(k1 - n * p)/snpq}')
#     print(f'x2= {(k2 - n * p)/snpq}')


# local_laplace()




n = int(input())
def even(x):
    for i in range(x):
        if i % 2 == 0: 
            yield str(i) + ','


a = ' '.join(list(even(n)))
print(a)
print(a[0:len(a)-1])
