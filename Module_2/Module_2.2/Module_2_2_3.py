def task(data):
    n, X, Y, A, B = map(int, data.split())
    X -= 1
    A -= 1
    lst = [i for i in range(1, n + 1)]
    lst = lst[:X] + lst[X:Y][::-1] + lst[Y:]
    lst = lst[:A] + lst[A:B][::-1] + lst[B:]

    return ' '.join(map(str, lst))
