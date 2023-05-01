def clock():
    n = 16
    num = 1

    def rec(n, num):
        if n > 4:
            print(' ' * num * 2 + (n * str(num)))
            rec(n - 4, num + 1)
        print(' ' * num * 2 + (n * str(num)))

    rec(n, num)


if __name__ == '__main__':
    clock()
    
