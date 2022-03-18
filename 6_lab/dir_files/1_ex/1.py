import os 

cwd = os.getcwd()

def only_directories(path):
    for root, dirs, files in os.walk(path):
        print(f'dir: {dirs}')
def only_directories_2(path):
    d = ([x for x in os.listdir(path) if os.path.isdir(x) == True])
    print(d)



def only_files(path):
    for root, dirs, files in os.walk(path):
        print(f'file: {files}')
def only_files_2(path):
    d = [x for x in os.listdir(path) if os.path.isfile(x) == True]
    print(d)



def all_dirs_files(path):
    for root, dirs, files in os.walk(path):
        print(f'dir: {dirs}')
        print(f'file: {files}')
        print('-*' * 10)

def all_dirs_files_2(path):
    d = [x for x in os.listdir(path)]
    print(d)

some_path = r'C:\Users\USER\Desktop\coding\PP2\6_lab'

all_dirs_files_2(some_path)
