def is_greater(lists, number):
    return any((sum(i) > number) for i in lists)
  
