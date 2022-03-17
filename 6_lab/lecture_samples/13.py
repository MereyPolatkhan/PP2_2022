import csv

# with open('test.csv', 'r') as f:
#     reader = csv.reader(f, delimiter = '*')
#     for i in reader:
#         print(i[0], i[1], i[2])


with open('test.csv', 'w') as f:
    writer = csv.writer(f, delimiter='*')
    for i in range(20):
        writer.writerow([f'name: {i}', f' age: {i}', f' adress: {i}'])