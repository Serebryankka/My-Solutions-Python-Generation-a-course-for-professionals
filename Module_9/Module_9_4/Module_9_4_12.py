def _print(*args, sep=' ', end='\n'):
    import sys
    sys.stdout.write(sep.upper().join(map(lambda x: x.upper() if isinstance(x, str) else str(x), args)) + end.upper())
    
    
print = _print
