def non_negative_even(numbers):
    return all((not(i % 2) and (i >= 0) for i in numbers))
  
