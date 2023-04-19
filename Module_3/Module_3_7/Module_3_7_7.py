import calendar


def main():
    return [print(calendar.isleap(int(input()))) for _ in range(int(input()))]


if __name__ == '__main__':
    main()
    
