from collections import defaultdict


def hash_as_key(objects):
    d = defaultdict(list)
    [d[hash(i)].append(i) for i in objects]
    for k, v in d.items():
        if len(v) == 1:
            d[k] = v[0]
    return dict(d)
  
