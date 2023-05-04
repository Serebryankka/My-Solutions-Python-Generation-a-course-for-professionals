def my_pow(number):
    return sum(map(lambda x: int(x[1]) ** x[0], enumerate(str(number), 1)))
  
