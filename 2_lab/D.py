n = int(input()) 
a = []
for i in range(n):
    b = []
    for j in range(n):
        if  n % 2 == 1:
            if i + j >= n - 1:
                b.append('#')   
            else:    
                b.append('.')
        else:
            if j - i <= 0:
                b.append('#')   
            else:    
                b.append('.')
    a.append(b)


for i in range(n):
    for j in range(n):
        print(a[i][j], end="")
    print()