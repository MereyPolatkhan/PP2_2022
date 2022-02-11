
big_a = []
while True:
    s = input() 
    if s == "0":
        break
    
    b = s.split()
    b.reverse()
    big_a.append(b)

big_a.sort()
# try with key=func

for i in range(len(big_a)):
    big_a[i].reverse()
    for j in range(len(big_a[i])):
        print(big_a[i][j], end=" ")
    print()


    
    
