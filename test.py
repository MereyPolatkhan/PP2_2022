n = int(input()) 

k = 0

def isPrime(n):
    f = 0
    for i in range(2, n //2):
        if (n % i == 0):
            f += 1
    if f == 0:
        return True
    else:
        return False 

a = []

for i in range(n + 1):
    if isPrime(i) == True:
        k += 1
        a.append(i) 

print(k) 
print(a)