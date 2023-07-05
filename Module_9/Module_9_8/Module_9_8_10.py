import functools


def returns_string(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        if isinstance(value, str):
            return value
        else:
            raise TypeError
    return wrapper
  
