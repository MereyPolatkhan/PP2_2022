s = input() 
new = ""
for i in s:
    if i.isalpha() == True or i == " ":
        new += i
a = new.split(' ')
a.sort()

b = []

for i in a:
    if i not in b:
        b.append(i)

print(len(b))
for i in b:
    print(i)