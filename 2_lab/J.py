n = int(input()) 

def is_ideal(s):
    uppercase_counter = 0
    lowercase_counter = 0
    number_counter = 0
    for i in s:
        if ord(i) >= 65 and ord(i) <= 90:
            uppercase_counter += 1
        if ord(i) >= 97 and ord(i) <= 122:
            lowercase_counter += 1
        if ord(i) >= 48 and ord(i) <= 57:
            number_counter += 1
    
    if uppercase_counter > 0 and lowercase_counter > 0 and number_counter > 0:
        return True
    else:
        return False

a = list()
for i in range(n):
    s = input() 
    if is_ideal(s) == True:
        if s not in a:
            a.append(s)


print(len(a))
a.sort()
for i in a:
    print(i)