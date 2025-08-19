import json

with open ('seuarquivo.json', 'r', encoding='utf-8' ) as jsonfile:
    data= json.load(jsonfile)
    print(data)