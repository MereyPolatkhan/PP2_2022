import re
import csv

with open('row.txt', 'r', encoding='utf-8') as f:
    text = f.read() 


# bin = re.search(r'БИН(?P<bin>.+)', text)
# if bin:
#     print(bin.group('bin').strip())

# ndc = re.search(r'НДС Серия(?P<ndc>.+)', text)
# if ndc:
#     print(ndc.group('ndc').strip())


res = re.search(r'БИН(?P<bin>.+)\nНДС Серия(?P<ndc>.+)', text)

if res:
    # print(res.group('bin').strip(), res.group('ndc').strip())
    BIN = res.group('bin').strip()
    NDC = res.group('ndc').strip()


bill_num = re.search(r'Порядковый номер чека(?P<bill_number>.+)', text).group('bill_number').strip() 
# print(bill_num)

products_pattern = r'(?P<name>.+)\n(?P<count>.+)x(?P<price>.+)\n(?P<total>.+)\nСтоимость\n(?P<total2>.+)'

data = [['БИН', 'НДС', 'номер чека', 'name', 'count', 'price', 'total', 'total2']]

products_res = re.finditer(products_pattern, text)

for res in products_res:
    data.append([
        BIN,
        NDC,
        bill_num,
        res.group('name').strip(),
        res.group('count').strip(),
        res.group('price').strip(),
        res.group('total').strip(),
        res.group('total2').strip()        
    ])

with open('products.csv', 'w', encoding='utf-8') as f:
    csv.writer(f).writerows(data)
