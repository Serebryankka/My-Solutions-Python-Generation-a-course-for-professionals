def tribonacci(n):
    cache = {1: 1, 2: 1, 3: 1}
    def rec(n):
        result = cache.get(n)
        if result is None:
            result = rec(n - 3) + rec(n - 2) + rec(n - 1)
            cache[n] = result
        return result
    return rec(n)
  
