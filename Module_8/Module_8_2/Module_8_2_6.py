def func(a, b):
    def rec(num):
        if num <= b:
            print(num)
            rec(num + 1)
    rec(a)
func(1, 100)
