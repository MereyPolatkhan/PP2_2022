import os, shutil

# os.mkdir('8_ex')
# shutil.move('8.py', '8_ex')

with open('delete_this_file.txt', 'w') as f:
    f.writelines(['hello', '\nkbtu'])

def delete_file(path):
    if os.path.exists(path) == True:
        os.remove(path)
    else:
        print('path does NOT exist')

d = os.path.join(os.getcwd(), 'delete_this_file.txt')

# delete_file(d)