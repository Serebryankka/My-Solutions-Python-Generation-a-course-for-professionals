def linear(nested_lists):
    result = []
    for i in nested_lists:
        if type(i) is list:
            result += linear(i)
        else:
            result.append(i)
    return result
