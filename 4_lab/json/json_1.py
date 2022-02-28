import json 

with open('sample-data.json', 'r') as f:
    data = f.read() 

a = json.loads(data)

# print(type(a)) --> dict 

print("Interface Status")
print('=' * 80)

print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------") 

for i in a["imdata"]:
    pass