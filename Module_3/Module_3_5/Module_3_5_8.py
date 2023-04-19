from datetime import datetime, timedelta


def choose_plural(amount, declension):
    amount = str(amount)
    if int(amount) % 100 != 11 and amount[-1] == '1':
        return f'{amount} {declension[0]}'
    elif int(amount) % 100 not in [12, 13, 14] and amount[-1] in '234':
        return f'{amount} {declension[1]}'
    else:
        return f'{amount} {declension[2]}'


def main(data):
    r = datetime(2022, 11, 8, 12) - datetime.strptime(data, '%d.%m.%Y %H:%M')
    days = ['день', 'дня', 'дней']
    hours = ['час', 'часа', 'часов']
    minutes = ['минута', 'минуты', 'минут']
    if r <= timedelta(seconds=0):
        return print('Курс уже вышел!')
    if r.days == 0 and (r.seconds / 60) // 60 == 0:  # Кол-во дней и часов 0
        print(f'До выхода курса осталось: {choose_plural(int(r.seconds / 60), minutes)}')
    elif r.days == 0:  # Кол-во дней 0
        print(f'До выхода курса осталось: {choose_plural(int((r.seconds / 60) / 60), hours)}', end='')
        if (r.seconds / 60) % 60:  # Кол-во минут > 0
            print(f' и {choose_plural(int((r.seconds / 60) % 60), minutes)}')
    else:  # Кол-во дней > 0
        print(f'До выхода курса осталось: {choose_plural(r.days, days)}', end='')
        if (r.seconds / 60) / 60:  # Кол-во часов > 0
            print(f' и {choose_plural(int((r.seconds / 60) / 60), hours)}')


if __name__ == '__main__':
    main(input())
    
