import re

def func(text):
    x = re.search("^[a-z]+_[a-z]+$", text)
    if x:
        print(f'found: {x.group()}')
    else:
        print(f'not found: {x}')

s = input() 
func(s)


def func2(text):
    x = re.findall("[a-z]+_[a-z]+", text)
    print(x)

func2(s)