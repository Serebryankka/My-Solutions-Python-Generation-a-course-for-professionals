from collections import Counter


for k, v in sorted(Counter(input().split(',')).items()):
    print(f'{k}: {v}')
    
