n = int(input()) 
a = []

a = [int(j) for j in input().split(" ")]

b = []
for i in range(n):
    for j in range(i):
        b.append(a[i] * a[j])

# print(b)
print(max(b))