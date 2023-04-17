from datetime import datetime


def main():
    with open('diary.txt', 'r', encoding='utf-8') as f:
        d = {}
        report = f.readline()
        d[report] = ''
        for line in f:
            if line == '\n':
                report = f.readline()
                d[report] = ''
                continue
            d[report] += line
        for k, v in sorted(d.items(), key=lambda x: datetime.strptime(x[0], '%d.%m.%Y; %H:%M\n')):
            print(k, v, sep='')
if __name__ == '__main__':
    main()
    
