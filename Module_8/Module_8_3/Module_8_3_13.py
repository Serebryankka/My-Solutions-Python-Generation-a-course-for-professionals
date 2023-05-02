def is_power(number):
    if number == 2 or number == 1:
        return True
    elif number % 2:
        return False
    else:
        return is_power(number / 2)
      
