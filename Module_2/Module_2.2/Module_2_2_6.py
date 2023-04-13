def task():
    data = (input() for _ in range(int(input())))
    data = list(map(lambda x: x.split(', '), data))
    result = set(data[0]).intersection(*data[1:])
    return 'Сериал снять не удастся' if not result else ", ".join(sorted(result))


if __name__ == '__main__':
    print(task())
