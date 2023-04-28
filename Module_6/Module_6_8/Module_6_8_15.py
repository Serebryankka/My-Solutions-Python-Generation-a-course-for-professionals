from collections import Counter


for k, v in sorted(Counter(map(len, input().split())).items(), key=lambda x: x[1]):
    print(f'Слов длины {k}: {v}')
  
