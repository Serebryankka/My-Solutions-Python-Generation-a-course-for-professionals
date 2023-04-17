from datetime import datetime, timedelta


def main(data):
    return int((datetime.strptime(data, '%H:%M:%S') - datetime(1900, 1, 1)).total_seconds())

if __name__ == '__main__':
    main(input())
    
