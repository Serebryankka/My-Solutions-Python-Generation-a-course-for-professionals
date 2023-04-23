import json
import sys


def main(data):
    data = json.load(data)
    for k, v in data.items():
        if type(v) == list:
            print(f'{k}: {", ".join(map(str,v))}')
        else:
            print(f'{k}: {v}')


if __name__ == '__main__':
    main(sys.stdin)
    
