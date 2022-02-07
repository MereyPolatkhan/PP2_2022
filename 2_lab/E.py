a = input().split()
n, x = 0, 0
if len(a) == 2:
    n = int(a[0])
    x = int(a[1])
else:
    n = int(a[0])
    x = int(input())


xor = 0
for i in range(n):
    xor = xor ^ (x + 2 * i)

print(xor)

