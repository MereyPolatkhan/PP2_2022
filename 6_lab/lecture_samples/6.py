import os

WORKING_DIR = os.getcwd() 

# print(WORKING_DIR)

def safe_folder_create(path):
    if os.path.exists(path) == False:
        os.mkdir(path) 
    else:
        print('path already exists')

print(os.path.exists('dir1'))
# os.mkdir('dir1')

safe_folder_create('dir2')

