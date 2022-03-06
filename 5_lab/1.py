import re

def func(text):
    x = re.search("^a(b*)$", text)
    if x:
        print(f'found: {x.group()}')
    else:
        print(f'not found: {x}')

s = input() 
func(s)