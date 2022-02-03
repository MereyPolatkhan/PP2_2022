s = str(input())
def binary_to_decimal(s):
    dec = 0
    s = s[::-1] 
    for i in range(len(s)-1, -1, -1):
        dec += 2 ** i * (ord(s[i]) - 48)
    return dec

print(binary_to_decimal(s))


i = 0
sum = 0
def recursion(s):
    global i, sum
    if(i == len(s)):
        return sum
    sum += 2**i * int(s[-1-i])
    i += 1
    return recursion(s)
print(recursion(s))