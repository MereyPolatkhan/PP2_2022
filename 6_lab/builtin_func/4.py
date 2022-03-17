import time, math


number = float(input('input number: '))

ms = float(input('input milliseconds: '))
s = ms * 0.001

time.sleep(s)
print(f'Square root of {int(number)} after {int(ms)} miliseconds is {math.sqrt(number)}')