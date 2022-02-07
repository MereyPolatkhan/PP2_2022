s1 = input() 
s = ""
for i in s1:
    if i == "{" or i == "}" or i == "(" or i == ")" or i == "[" or i == "]":
        s = s + i

a = list() 
ok = True

for i in s:
    if i == "{" or i == "(" or i == "[":
        a.append(i)

    else:
        if len(a) == 0:
            ok = False
            break
        else:
            if i == "}" and a[-1] == "{":
                del a[-1]
            elif i == "]" and a[-1] == "[":
                del a[-1]
            elif i == ")" and a[-1] == "(":
                del a[-1]
            else:
                ok = False
                break 
if len(a) == 0 and ok == True:
    print("Yes")
else:
    print("No")

