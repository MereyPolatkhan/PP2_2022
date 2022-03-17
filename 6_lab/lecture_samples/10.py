import os 

cwd = os.getcwd() 

# os.makedirs('f1/f3')

for root, dirs, files in os.walk(cwd):
    print(f'root: {root}')
    print(f'dirs: {dirs}')
    print(f'files: {files}')
    print('----'*10)

print('-*-'*20)

for root, dirs, files in os.walk('.'):
    print(f'root: {root}')
    print(f'dirs: {dirs}')
    print(f'files: {files}')
    print('----'*10)