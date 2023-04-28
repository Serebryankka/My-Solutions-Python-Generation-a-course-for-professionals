from collections import Counter


words = Counter(input().lower().split())
min_value = min(words.values())
val = min_value
result = []


for i in range(1, len(words)+1):
    w = words.most_common()[-i]
    val = w[1]
    if val == min_value:
        result.append(w[0])
print(*sorted(result), sep=', ')
