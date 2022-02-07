d = {
    "ONE": 1,
    "TWO": 2,
    "THR": 3,
    "FOU": 4,
    "FIV": 5,
    "SIX": 6,
    "SEV": 7,
    "EIG": 8,
    "NIN": 9,
    "ZER": 0,
}

s = input().split("+")
a1 = s[0]
a = a1.replace(a1[-1], "")
a_list = []
for i in range(0, len(a), 3):
    a_list.append(a[i:i+3])

b1 = s[1]
b = b1.replace(b1[0], "")
b_list = []
for i in range(0, len(b), 3):
    b_list.append(b[i:i+3])

num1 = ""
num2 = ""
for i in a_list:
    num1 = num1 + str(d[i])
for i in b_list:
    num2 = num2 + str(d[i])
print(num1, num2)