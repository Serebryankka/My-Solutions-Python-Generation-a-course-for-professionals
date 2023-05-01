def print_digits(number):
    number = str(number)
    length = len(number)

    def rec(n):
        if n < length:
            rec(n + 1)
            print(number[n])
    rec(0)
    
