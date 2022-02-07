s = input() 
new = ""
for i in s:
    if i.isalpha() == True or i == " ":
        new += i


a = new.split(' ')

a.sort()
print(len(a))
for i in a:
    print(i)