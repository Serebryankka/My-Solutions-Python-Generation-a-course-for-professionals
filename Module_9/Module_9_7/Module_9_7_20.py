def upper_case(func):
    def wrapper(*args, **kwargs):
        args = (str(arg).upper() for arg in args)
        kwargs = {k: v.upper() for k, v in kwargs.items()}
        return func(*args, **kwargs)
    return wrapper

print = upper_case(print)
  
