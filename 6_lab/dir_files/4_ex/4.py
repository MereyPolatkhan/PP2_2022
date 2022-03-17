import os
import shutil 

def file_line_counter(file):
    k = 0
    f = open(file, 'r') 
    for line in f:
        # print(line)
        k += 1
    print('number of line:', k)

file = '4_ex.txt'

file_line_counter(file)

# os.mkdir('4_ex')
# shutil.move('4_ex.txt', '4_ex')
# shutil.move('4.py', '4_ex')
