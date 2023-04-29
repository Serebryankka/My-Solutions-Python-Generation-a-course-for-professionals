from collections import ChainMap

with open('zoo.json', encoding='utf-8') as json_file:
    print(sum(ChainMap(*(json.load(json_file))).values()))
    
