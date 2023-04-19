import time


def get_the_fastest_func(funcs, arg):
    min_time = float('inf')
    for func in funcs:
        start_time = time.perf_counter()
        func(arg)
        time_taken = time.perf_counter() - start_time
        if time_taken < min_time:
            min_time = time_taken
            the_fastest_func = func
    return the_fastest_func
  
