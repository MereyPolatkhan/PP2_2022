n = int(input())
demons = dict()

for i in range(n):
  a = input().split() 
  if a[1] in demons:
    demons[a[1]] = demons[a[1]] + 1
  else:
    demons[a[1]] = 1


m = int(input()) 
hunters = dict() 

for i in range(m):
  b = input().split() 
  if b[1] in hunters:
    hunters[b[1]] = hunters[b[1]] + int(b[2])
  else:
    hunters[b[1]] = int(b[2])

# print(hunters)

# demons = {'water': 3, 'thunder': 1, 'sun': 1}
# hunters = {'water': 21, 'thunder': 1}

k = 0

for key_demon in demons.keys():
  if key_demon in hunters:
    if hunters[key_demon] - demons[key_demon] < 0:
      k += 1
  else:
    k += 1

print(f'Demons left: {k}')
