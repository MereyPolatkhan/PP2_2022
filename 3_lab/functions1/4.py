def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    
arr = list(filter(lambda x: isPrime(x), [int(i) for i in input().split(' ')]))

print(arr)