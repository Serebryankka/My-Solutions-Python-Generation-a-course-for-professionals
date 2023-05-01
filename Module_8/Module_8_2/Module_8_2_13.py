def print_digits(number):
    number = str(number)
    length = len(number)

    def rec(n):
        if n < length:
            print(number[n])
            rec(n + 1)

    rec(0)
    
