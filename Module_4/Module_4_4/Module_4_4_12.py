import json
import csv


with open('students.json', 'r', encoding='utf-8') as f:
    result = []
    for d in json.load(f):
        if int(d['age']) >= 18 and int(d['progress']) >= 75:
            result.append({'name': d['name'], 'phone': d['phone']})
    result.sort(key=lambda x: x['name'])
with open('data.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'phone'])
    writer.writeheader()
    writer.writerows(result)
    
