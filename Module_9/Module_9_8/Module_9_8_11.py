import functools


def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        print(f'''TRACE: вызов {func.__name__}() с аргументами: {args}, {kwargs}
TRACE: возвращаемое значение {func.__name__}(): {value}''')
        return value
    return wrapper
