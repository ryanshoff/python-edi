#from bots.botsconfig import *
from records003040 import recorddefs

structure = [
    {'ID': 'ISA', 'MIN': 1, 'MAX': 1},
    {'ID': 'GS', 'MIN': 1, 'MAX': 1},
    {'ID': 'ST', 'MIN': 1, 'MAX': 1},
    {'ID': 'BSN', 'MIN': 1, 'MAX': 1},
    {'ID': 'NTE', 'MIN': 0, 'MAX': 100},
    {'ID': 'DTM', 'MIN': 0, 'MAX': 10},
    {'ID': 'HL', 'MIN': 1, 'MAX': 1, 'LEVEL': [
        {'ID': 'MEA', 'MIN': 0, 'MAX': 40},
        {'ID': 'TD1', 'MIN': 0, 'MAX': 20},
        {'ID': 'TD5', 'MIN': 0, 'MAX': 12},
        {'ID': 'TD3', 'MIN': 0, 'MAX': 12},
        {'ID': 'REF', 'MIN': 0, 'MAX': 200},
        {'ID': 'FOB', 'MIN': 0, 'MAX': 1},
        {'ID': 'N1', 'MIN': 0, 'MAX': 200},
        {'ID': 'HL', 'MIN': 1, 'MAX': 200000, 'LEVEL': [
            {'ID': 'LIN', 'MIN': 0, 'MAX': 1},
            {'ID': 'SN1', 'MIN': 0, 'MAX': 1},
            {'ID': 'SLN', 'MIN': 0, 'MAX': 100},
            {'ID': 'PRF', 'MIN': 0, 'MAX': 1},
            {'ID': 'PID', 'MIN': 0, 'MAX': 200},
            {'ID': 'MEA', 'MIN': 0, 'MAX': 40},
            {'ID': 'REF', 'MIN': 0, 'MAX': 200},
            {'ID': 'CLD', 'MIN': 1, 'MAX': 200, 'LEVEL': [
                {'ID': 'REF', 'MIN': 1, 'MAX': 200},
            ]},
            {'ID': 'CUR', 'MIN': 0, 'MAX': 1},
            {'ID': 'ITA', 'MIN': 0, 'MAX': 10},
        ]},
    ]},
    {'ID': 'CTT', 'MIN': 1, 'MAX': 1},
    {'ID': 'SE', 'MIN': 1, 'MAX': 1},
    {'ID': 'GE', 'MIN': 1, 'MAX': 1},
    {'ID': 'IEA', 'MIN': 1, 'MAX': 1},
]

def printelements(elements):
    print('"elements": [' )
    first = ''
    for element in elements[1:-1]:
        print(first)
        first = ','
        print('{ "id": "' + element[0] + '", ')
        print('"type": "element", ')
        print('"name": "",')
        print('"req": "' + ('M' if element[1] == 'M' else 'O') + '",')
        print('"data_type": "' + element[3] + '", ')
        print('"data_type_ids": null,') 
        print('"length": {"min": ', end='') 
        if isinstance(element[2], tuple):
            print(element[2][0], end='')
        else:
            print(str(1), end='')
        print(', "max": ', end='')
        if isinstance(element[2], tuple):
            print(element[2][1], end='')
        else:
            print(element[2], end='')
        print('},')
        print('"notes": "" }')
    print(']')


def printsegment(segment, first):
    print(first)
    print('{ "id": "' + segment['ID'] + '", "type": "segment",')
    print('"name": "", ')
    print('"req": "' + ('M' if segment['MIN'] else 'O') + '",')
    print('"max_uses": ' + str(segment['MAX']) + ',')
    print('"notes": "",')
    if segment['ID'] in recorddefs:
        printelements(recorddefs[segment['ID']])
    print('}')
    if 'LEVEL' in segment:
        first = ','
        for level in segment['LEVEL']:
            printsegment(level, first)

print('[')

first = ''
for segment in structure:
    if 'LEVEL' in segment:
        print(first)
        print('{"id":  "L_' + segment['ID'] + '", "type": "loop",')
        print('"name": "",')
        print('"req": "' + ('M' if segment['MIN'] else 'O') + '",')
        print('"repeat": ' + str(segment['MAX']) + ',')
        print('"segments": [')
        first = ''

    printsegment(segment, first)
    first = ','

    if 'LEVEL' in segment:
        print(']')
        print('}')
print(']')

