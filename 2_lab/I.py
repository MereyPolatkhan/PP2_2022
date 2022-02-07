n = int(input()) 

b = []
res = []
for i in range(n):
    s = input().split()
    if len(s) == 2: # [1, discovery]
        b.insert(len(b), s[1])
    else:
        res.append(b[0])
        del b[0]

for i in res:
    print(i, end=" ")