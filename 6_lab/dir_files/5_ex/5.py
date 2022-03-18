import os

def list_to_file(a):
    with open('list_to_file.txt', 'w') as f:
        for i in a:
            f.write(f'{i}\n')

a = [x for x in input().split()]

list_to_file(a)

