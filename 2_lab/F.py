n = int(input()) 
d = dict() 

for i in range(n):
  a = input().split()
  if a[0] in d:
    d[a[0]] = d[a[0]] + int(a[1])
  else:
    d[a[0]] = int(a[1])

max = -1

for val in d.values():
  if(val > max):
    max = val 

list_dict = sorted(d)

for i in range(len(list_dict)):
  if d[list_dict[i]] != max:
    print(f'{list_dict[i]} has to receive {max - d[list_dict[i]]} tenge')
  else:
    print(f'{list_dict[i]} is lucky!') 