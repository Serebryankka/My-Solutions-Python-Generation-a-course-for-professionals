import functools


def make_html(tag):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            return f'<{tag}>{value}</{tag}>'
        return wrapper
    return decorator
  
