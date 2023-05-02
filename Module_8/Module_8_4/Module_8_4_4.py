def recursive_sum(nested_lists):
    total = int()
    for i in nested_lists:
        if type(i) is int:
            total += i
        else:
            total += recursive_sum(i)
    return total
           
