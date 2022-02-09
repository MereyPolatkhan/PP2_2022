def string_calculator(str_input):  
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

    back_to_d = {
        "1": "ONE",
        "2": "TWO",
        "3": "THR",
        "4": "FOU",
        "5": "FIV",
        "6": "SIX",
        "7": "SEV",
        "8": "EIG",
        "9": "NIN",
        "0": "ZER",
    }


    s = str_input.split("+")
    a = s[0]
    a_list = []
    for i in range(0, len(a), 3):
        a_list.append(a[i:i+3])

    b = s[1]
    b_list = []
    for i in range(0, len(b), 3):
        b_list.append(b[i:i+3])

    # print(a_list, b_list)

    num1 = ""
    num2 = ""
    for i in a_list:
        num1 = num1 + str(d[i])
    for i in b_list:
        num2 = num2 + str(d[i])

    num = str(int(num1) + int(num2))

    for i in num:
        print(back_to_d[i], end="")

s = input()
string_calculator(s) # why size 777 -> 1025 when func is added
