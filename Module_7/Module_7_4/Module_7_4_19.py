def get_id(names, name):
    if type(name) is not str:
        raise TypeError('Имя не является строкой')
    elif not name.isalpha() or name != name.capitalize():
        raise ValueError('Имя не является корректным')
    return len(names) + 1
    
