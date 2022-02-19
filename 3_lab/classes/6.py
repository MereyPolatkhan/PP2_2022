def isPrime(number):
    if number < 2:
        return False

    for i in range(2, number//2 + 1):
        if number % i == 0:
            return False
        
    return True


arr = list(filter(lambda x: isPrime(x), [int(i) for i in input().split()]))

print(arr)