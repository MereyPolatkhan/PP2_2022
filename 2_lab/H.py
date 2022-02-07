xy1 = input().split() 
x1 = int(xy1[0])
y1 = int(xy1[1])

def distance2(x1, y1, x2, y2):
    return (x2 - x1)**2 + (y2 - y1)**2 

def fel(s):
    a = s.split() 
    return int(a[0])

coor_dist = dict()

n = int(input()) 

for i in range(n):
    xy2 = input().split() 
    x2 = int(xy2[0])
    y2 = int(xy2[1])

    coor_dist[str(distance2(x1, y1, x2, y2)) + " " + str(i)] = " ".join(xy2)

# print(coor_dist)

list_of_dist = sorted(coor_dist)

list_of_dist.sort(key = fel)

for dist in list_of_dist:
    print(coor_dist[dist])
