a = []
while True:
    n = int(input()) 
    if n == 0:
        break
    a.append(n)

b = []

for i in range(len(a)//2):
    b.append(a[i] + a[-1 - i])
        
if len(a) % 2 == 1:
    b.append(a[len(a)//2])

for i in b:
    print(i, end=" ")