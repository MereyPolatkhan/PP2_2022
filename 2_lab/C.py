n = int(input()) 
a = []

for i in range(n):
    b = []
    for j in range(n):
        if i == j:
            b.append(i * j)
        elif i == 0:
            b.append(j)
        elif j == 0:
            b.append(i)
        else:
            b.append(0)
    a.append(b)

for i in range(n):
    for j in range(n):
        print(a[i][j], end=" ")
    print()
