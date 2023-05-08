def sort_priority(values, group):
    return values.sort(key=lambda x: (x not in group, x))
