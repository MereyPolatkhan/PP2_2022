a = [int(i) for i in input().split()] 

i = 0
max_i = 0

flag = 1 # ok = True/False

while(i < len(a)):
    if max_i < i:
        flag = 0
        break
    if a[i] + i > max_i: # i = 5 > max_i ==> false
        max_i = a[i] + i 
    if max_i >= len(a) - 1:
        flag = 1
        break
    i += 1


print(flag)