def toLowercase(s):
    new = ""
    for i in range(len(s)):
        if ord(s[i]) >= 65 and ord(s[i]) <= 90:
            new += chr(ord(s[i]) + 32)
        else:
            new += s[i]
    return new

t = str(input())
print(toLowercase(t))
