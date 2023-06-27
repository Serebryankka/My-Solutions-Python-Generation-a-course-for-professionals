def get_digits(number: int | float) -> list[int]:
    return [int(s) for s in str(number).replace('.', '')]
  
