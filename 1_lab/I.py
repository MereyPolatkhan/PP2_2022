n = int(input()) 

for i in range(n):
    s = str(input()) 
    if '@gmail.com' in s:
        s = s.replace('@gmail.com', '')
        print(s)
        # print(s.removesuffix("gmail.com"))
