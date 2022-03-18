import re


def counter_upper_lower(s):
    up = re.findall(r'[A-Z]', s)
    low = re.findall(r'[a-z]', s)
    return f'Uppercase: {len(up)} \nLowercase: {len(low)}'
    

s = 'HelloWORldOEAFEAffsfse'
print(counter_upper_lower(s))


def counter_upper_lower_2(s):
    lo = 0
    up = 0 
    for i in s:
        if i.islower() == True:
            lo += 1
        if i.isupper() == True:
            up += 1
    return f'Uppercase: {(up)} \nLowercase: {(lo)}'
    
print(counter_upper_lower_2(s))
