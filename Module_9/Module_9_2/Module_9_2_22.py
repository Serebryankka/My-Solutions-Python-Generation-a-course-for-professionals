func = input()
a, b = [int(n) for n in input().split()]
max_value = max(eval(func) for x in range(a, b + 1))
min_value = min([eval(func) for x in range(a, b + 1)])
print(f'Минимальное значение функции {func} на отрезке [{a}; {b}] равно {min_value}')
print(f'Максимальное значение функции {func} на отрезке [{a}; {b}] равно {max_value}')
