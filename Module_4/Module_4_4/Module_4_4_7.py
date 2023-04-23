import json


with open('updated_data.json', 'w', encoding='utf-8') as upd_file, open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    result = []
    for i in data:
        if type(i) is str:
            result.append(f'{i}!')
        elif type(i) is int:
            result.append(i+1)
        elif type(i) is bool:
            result.append(not i)
        elif type(i) is list:
            result.append(i * 2)
        elif type(i) is dict:
            i['newkey'] = None
            result.append(i)
        elif type(i) is None:
            continue
    json.dump(result, upd_file, indent=3)
    
