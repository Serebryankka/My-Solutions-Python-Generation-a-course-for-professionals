def func(n):
    if not n:
        return 0
    else:
        return int(n[0]) + func(n[1:])


print(func(input()))
