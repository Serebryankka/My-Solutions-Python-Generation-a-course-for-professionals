def convert(number):
    if number < 0:
        x = 3
    else:
        x = 2
    return bin(number)[x:], oct(number)[x:], hex(number)
  
