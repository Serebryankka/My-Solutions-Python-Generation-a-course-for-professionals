import calendar, locale


locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

def get_weekday(number):
    if type(number) is not int:
        raise TypeError('Аргумент не является целым числом')
    number = int(number)
    if number < 1 or number > 7:
        raise ValueError('Аргумент не принадлежит требуемому диапазону')
    return calendar.day_name[number-1].title()
    
