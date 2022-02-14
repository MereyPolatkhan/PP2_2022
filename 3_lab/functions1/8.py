def spy_game(a):
    b = []
    for i in range(len(a)):
        if a[i] == 0 or a[i] == 7:
            b.append(a[i])
    #print(b)
    for i in range(len(b)-2):
        if b[i] == 0 and b[i + 1] == 0 and b[i + 2] == 7:
            return True
    
    return False


print(spy_game([1,2,4,0,0,7,5])) #--> True
print(spy_game([1,0,2,4,0,5,7])) #--> True
print(spy_game([1,7,2,0,4,5,0])) #--> False