import time


def calculate_it(func, *args):
    s = time.perf_counter()
    f = func(*args)
    return f, time.perf_counter() - s
  
