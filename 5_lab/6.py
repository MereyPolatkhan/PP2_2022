import re

def colon(text):
    x = re.sub("\s|,|[.]", ":", text)
    # x = re.sub("[ ,.]", ":", text)

    print(x)

s = input() 
colon(s)