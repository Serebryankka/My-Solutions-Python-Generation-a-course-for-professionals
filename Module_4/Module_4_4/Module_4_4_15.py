from collections import defaultdict
import json


with open('food_services.json ', 'r', encoding='utf-8') as f:
    d = defaultdict(lambda: defaultdict(int))
    for rest in json.load(f):
        d['District'][rest['District']] += 1
        if rest['OperatingCompany']:
            d['OperatingCompany'][rest['OperatingCompany']] += 1
            
for i in d:
    tup = max(d[i].items(), key=lambda x: x[1])
    print(f'{tup[0]}: {tup[1]}')
    
