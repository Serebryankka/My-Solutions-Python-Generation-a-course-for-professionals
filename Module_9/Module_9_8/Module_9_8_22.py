import functools


def takes(*types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            for arg in *args, *kwargs.values():
                if not any([isinstance(arg, t) for t in types]):
                    raise TypeError
            return value
        return wrapper
    return decorator
  
