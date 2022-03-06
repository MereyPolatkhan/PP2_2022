import re

def func(text):
    x = re.sub("\s|,|[.]", ":", text)
    # x = re.sub("[ ,.]", ":", text)

    print(x)

s = input() 
func(s)