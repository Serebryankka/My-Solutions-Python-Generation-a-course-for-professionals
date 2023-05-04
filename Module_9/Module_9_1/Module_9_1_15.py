def zip_longest(*args, fill=None):
    length = len(max(args, key=len))
    for i in args:
        diff = length - len(i)
        if diff:
            i.extend([fill] * diff)
    return list(zip(*args))
  
