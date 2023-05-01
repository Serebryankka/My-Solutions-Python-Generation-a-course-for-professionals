def func(num):
    if not num:
        return 0
    else:
        return 1 + func(num[1:])
      
