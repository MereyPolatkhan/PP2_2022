import os 
import string 

def letters():
    for i in string.ascii_uppercase:
        with open(i + '.txt', 'w') as f:
            f.write(i)

letters()