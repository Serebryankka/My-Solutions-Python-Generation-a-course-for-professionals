def recursive_sum(a, b):
    if not b:
        return a
    else:
        return recursive_sum(a + 1, b - 1)
      
