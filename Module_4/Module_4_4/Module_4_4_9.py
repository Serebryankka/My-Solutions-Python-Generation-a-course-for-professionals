import json


with open('people.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    max_dict = max(data, key=len)
    for i, d in enumerate(data):
        for k in max_dict.keys():
            if k not in d:
                data[i][k] = None
with open('updated_people.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=3)
