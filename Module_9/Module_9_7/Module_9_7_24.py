def takes_positive(func):
    def wrapper(*args, **kwargs):
        if not all([isinstance(arg, int) for arg in args]):
            raise TypeError
        elif not all([arg > 0 for arg in args]):
            raise ValueError
        else:
            return func(*args, **kwargs)
    return wrapper
  
