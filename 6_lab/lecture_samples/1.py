f = open('input.txt', 'r') 
# print(f.read())
# print(f.readlines())

# for i in f.readlines():
#     print(i)


for i in f:
    print(i)

f.close()