"""
Following values can be passed as the mode parameter of access() to test the following:

os.access(path, mode)

os.F_OK: Tests existence of the path.
os.R_OK: Tests readability of the path.
os.W_OK: Tests writability of the path.
os.X_OK: Checks if path can be executed. / executability
"""

import os

cwd = os.getcwd() 

def existence(path):
    if os.access(path, os.F_OK) == True:
        print('the path exists: ', True)
    else:
        print('the path does NOT exist: ', False)

def readability(path):
    if os.access(path, os.R_OK) == True:
        print('path is readable: ', True)
    else:
        print('path is NOT readable: ', False)

def writability(path):
    if os.access(path, os.W_OK) == True:
        print('path is writable: ', True)   
    else:
        print('path is NOT writable: ', False)

def executability(path):
    if os.access(path, os.X_OK) == True:
        print('path is executable: ', True)
    else:
        print('path is NOT executable: ', False)


print('current working directory: ', cwd)
existence(cwd)
readability(cwd)
writability(cwd)
executability(cwd)

print('-*'*10)

path = r'C:\Users\USER\Desktop\coding\PP2\6_lab'
existence(path)
readability(path)
writability(path)
executability(path)