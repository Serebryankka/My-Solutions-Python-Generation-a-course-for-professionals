def custom_isinstance(objects, typeinfo):
    return sum((isinstance(i, typeinfo) for i in objects))
  
