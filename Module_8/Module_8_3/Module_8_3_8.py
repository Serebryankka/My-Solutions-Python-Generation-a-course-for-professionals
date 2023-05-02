def number_of_frogs(year):
    cache = {1: 77, 2: 141}

    def rec(year):
        result = cache.get(year)
        if result is None:
            result = 3 * (rec(year - 1) - 30)
            cache[year] = result
        return result

    return rec(year)
  
