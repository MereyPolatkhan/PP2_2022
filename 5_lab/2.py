import re

def func(text):
    x = re.search("ab{2,3}", text)
    if x:
        print(f'found: {x.group()}')
    else:
        print(f'not found: {x}')

s = input() 
func(s)