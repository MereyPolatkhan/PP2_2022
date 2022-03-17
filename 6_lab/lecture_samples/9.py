import os 

WORKING_DIR = os.getcwd() 

def show_dir_content(path, depth = 1):
    for item in os.listdir(path):
        target_path = os.path.join(path, item) 
        if os.path.isfile(target_path):
            print('---' * depth, end=' ') 
            print(f'file: {item}')
        
        if os.path.isdir(target_path):
            print('---' * depth, end=' ') 
            print(f'dir: {item}')
            show_dir_content(target_path, depth + 1)

os.chdir('..')
new_path = os.getcwd() 

show_dir_content(new_path)