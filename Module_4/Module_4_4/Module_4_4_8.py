import json


with open('data1.json', 'r', encoding='utf-8') as f1, open('data2.json', 'r', encoding='utf-8') as f2:
    data1 = json.load(f1)
    data1.update(json.load(f2))
with open('data_merge.json', 'w', encoding='utf-8') as file:
    json.dump(data1, file, ensure_ascii=False, indent=4)
    
