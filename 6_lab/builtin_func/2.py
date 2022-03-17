import re


def counter_upper_lower(s):
    up = re.findall(r'[A-Z]', s)
    low = re.findall(r'[a-z]', s)
    return f'Uppercase: {len(up)} \nLowercase: {len(low)}'
    

s = 'KBtuFITis'
print(counter_upper_lower(s))