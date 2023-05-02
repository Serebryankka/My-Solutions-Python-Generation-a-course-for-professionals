def get_fast_pow(a, b):
    if not b:
        return 1
    elif b % 2:
        return a * get_fast_pow(a, b - 1)
    else:
        return get_fast_pow(a*a, b / 2)
        
