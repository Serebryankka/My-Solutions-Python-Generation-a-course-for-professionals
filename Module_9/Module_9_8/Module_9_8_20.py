import functools


def strip_range(start, end, char='.'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            if end > len(value):
                result = value[:start] + char * len(value[start:])
            else:
                result = value[:start] + char * (end - start) + value[end:]
            return result
        return wrapper
    return decorator
