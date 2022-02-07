s = str(input())
a = s.split()

for i in a:
    if len(i) >= 3:
        print(i, end=" ")

