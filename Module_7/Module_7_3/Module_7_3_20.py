import calendar


try:
    n = int(input())
    print(('Введено число из недопустимого диапазона',calendar.month_name[n])[0 < n < 13])
except IndexError:
    print('Введено число из недопустимого диапазона')
except ValueError:
    print('Введено некорректное значение')
    
