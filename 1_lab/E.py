s = input().split(' ')

dist = int(s[0])
count = int(s[1])

# to know second way of reading integers in one line !!!! 

def isPrime(n):
    k = 0
    for i in range(2, n // 2):
        if n % i == 0:
            k = k + 1
    if k == 0:
        return True
    else:
        return False

if(dist <= 500 and isPrime(dist) == True and count % 2 == 0):
    print("Good job!")
else:
    print("Try next time!")