from collections import Counter


lst = Counter(input().split(','))
max_len = len(max(lst, key=len))
for k, v in sorted(lst.items()):
    unicode = sum((ord(i) for i in k if i.isalpha()))
    price = unicode * v
    print(f'{k.ljust(max_len)}: {unicode} UC x {v} = {price} UC')
    
