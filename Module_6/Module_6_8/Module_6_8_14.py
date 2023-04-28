from collections import Counter


words = Counter(input().lower().split()).most_common()
print(max(words, key=lambda x: (x[1], x[0]))[0])
