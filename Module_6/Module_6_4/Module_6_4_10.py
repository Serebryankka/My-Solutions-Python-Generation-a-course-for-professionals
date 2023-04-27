import pickle
from collections import namedtuple


Animal = namedtuple('Animal', 'name,family,sex,color')

with open('data.pkl', 'rb') as file:
    data = pickle.load(file)
    
for tup in data:
    for k, v in zip(tup._fields, tup):
        print(f'{k}: {v}')
    print()
    
