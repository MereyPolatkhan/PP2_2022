import json 

with open('sample-data.json', 'r') as f:
    a = json.load(f)

# print(type(a)) --> dict 

with open('output.txt', 'w') as out:
    print("Interface Status", file = out)
    print('=' * 80, file = out)
    print("DN                                                 Description           Speed    MTU  ", file = out)
    print("-------------------------------------------------- --------------------  ------  ------", file = out) 
    for i in a['imdata']:
        dn = i['l1PhysIf']['attributes']['dn']
        descr = i['l1PhysIf']['attributes']['descr']
        speed = i['l1PhysIf']['attributes']['speed']
        mtu = i['l1PhysIf']['attributes']['mtu']
        print(f'{dn}\t\t\t\t\t\t{descr}\t\t{speed}   {mtu}', file = out)
        



