def has_33(a):
    k = 0
    for i in range(len(a)-1):
        if a[i] == 3 and a[i + 1] == 3:
            k += 1
    if k == 0:
        return False
    else:
        return True

print(has_33([1, 3, 3]))  
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))