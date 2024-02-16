import json

print('Interface Status')
print('=======================================================================================')
print('DN                                                 Description           Speed    MTU')
print('-------------------------------------------------- --------------------  ------  ------')


with open('sample-data.json', 'r') as file:
    sample_data = json.load(file)

    for object in sample_data['imdata']:
        attr = object['l1PhysIf']['attributes']

        dn = attr['dn']
        descr = attr['descr']
        speed = attr['speed']
        MTU = attr['mtu']

        print(f'{dn}         {descr}                     {speed}   {MTU}')