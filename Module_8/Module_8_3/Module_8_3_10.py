def get_pow(a, b):
    if not b:
        return 1
    else:
        return a * get_pow(a, b - 1)
      
