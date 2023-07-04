def do_twice(func):
    def wrapper(*agrs, **kwargs):
        func(*agrs, **kwargs)
        func(*agrs, **kwargs)
    return wrapper
   
