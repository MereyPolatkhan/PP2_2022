import os 

cwd = os.getcwd() 

if os.path.exists('dir1'):
    os.rename('dir1', 'dir1_changed')

# os.rmdir('dir1_changed/dir1_1')
os.rmdir('dir1_changed')



