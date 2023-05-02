def range_sum(numbers, start, end):
    if start == end:
        return numbers[start]
    return numbers[start] + range_sum(numbers, start + 1, end)
  
