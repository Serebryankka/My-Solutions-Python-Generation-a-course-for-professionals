from collections import Counter


with open('pythonzen.txt', encoding='utf-8') as f:
    for k, v in sorted(Counter((s.lower() for s in f.read() if s.isalpha())).items()):
        print(f'{k}: {v}')
        
