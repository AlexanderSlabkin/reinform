#!/usr/env python3
import os
import requests
import pickle
import json


print(os.getcwd())
program = requests.get('https://gis.reinform-int.ru/geoserver/www/dictionaries/mr_program_BasesInclusion_1.json')
print(program.text)

data = json.loads(program.text)
items = set()
with open('program_names.pickle', 'wb') as file:
    for item in data:
        items.add(item['name'])

    print(items)
    pickle.dump(items, file)

items = {}
with open('program_names.json', 'w') as file:
    for index, item in enumerate(data):
        items[str(index)] = item['name']
    json.dump(items, file)

from qgis.core import *
with open('str.txt', 'w') as file:
    for item in data:
        file.write(item['name']+'\n')