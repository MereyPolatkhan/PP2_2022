import re

def func(text):
    x = re.search("^[a-z]+_[a-z]+$", text)
    if x:
        print(f'found: {x.group()}')
    else:
        print(f'not found: {x}')

s = input() 
func(s)
