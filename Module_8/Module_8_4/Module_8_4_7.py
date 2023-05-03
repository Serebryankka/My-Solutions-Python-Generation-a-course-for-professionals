def get_all_values(nested_dicts, key):
    result = set()
    if key in nested_dicts:
        result.add(nested_dicts[key])
    for k, v in nested_dicts.items():
        if type(v) is dict:
            value = get_all_values(v, key)
            if value is not None:
                result |= (value)
    return result
    
