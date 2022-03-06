import re

def toCamel(text):
    x = re.split("[_]", text)
    print(x[0], end="")
    for i in range(1, len(x)):
        print(x[i].capitalize(), end="")

s = input() 
toCamel(s)
