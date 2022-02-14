def unique(a):
    new = []
    for el in a:
        if el not in new:
            new.append(el)
    return(new)

print(unique([int(i) for i in input().split()]))