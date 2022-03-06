import re

def func(text):
    x = re.findall("[A-Z][a-z]+", text)
    print(x)

s = input() 
func(s)