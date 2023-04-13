def task(data):
    data = data.split()
    return ' '.join(sorted(set(filter(lambda x: data.count(x) > 1, data)), key=int))
