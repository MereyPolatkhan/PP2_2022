s = input()
a = s.split()

for i in range(len(a)):
    if len(a[i]) < 3:
        del a[i]
        # i -= 1
        
print(a)