import os

cwd = os.getcwd() 

def checker(path):
    if os.path.exists(path) == True:
        print('the filename: ', os.path.basename(path))
        print('the directory: ', os.path.dirname(path))
    else:
        print('path does NOT exist')
print(f'current working DIR: {cwd}')
checker(cwd)