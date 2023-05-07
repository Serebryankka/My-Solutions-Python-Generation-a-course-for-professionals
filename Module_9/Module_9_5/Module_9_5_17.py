def generator_square_polynom(a, b, c):
    def func(x):
        return a * x ** 2 + b * x + c
    return func
