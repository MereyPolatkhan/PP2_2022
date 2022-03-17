import os 

WORKING_DIR = os.getcwd() 

def safe_folder_create(path):
    if os.path.exists(path) == False:
        os.mkdir(path)
    else:
        print('path already exists')

# print(os.path.isdir(WORKING_DIR)) # True
# print(os.path.isfile(WORKING_DIR)) # False
# print(WORKING_DIR) # C:\Users\USER\Desktop\coding\PP2\6_lab\lecture_samples

# print(os.path.isdir('C:\Users\USER\Desktop\coding\PP2\6_lab\lecture_samples'))


# print(os.listdir('.') == os.listdir(WORKING_DIR))

for item in os.listdir(WORKING_DIR):
    # target_path = WORKING_DIR + "\\" + item # not recommended
    target_path = os.path.join(WORKING_DIR, item)
    # print(target_path)

    if os.path.isdir(target_path) == True:
        print(f'dir: {item}')
        for item2 in os.listdir(target_path):
            print('---', item2)


    if os.path.isfile(target_path) == True:
        print(f'file: {item}')