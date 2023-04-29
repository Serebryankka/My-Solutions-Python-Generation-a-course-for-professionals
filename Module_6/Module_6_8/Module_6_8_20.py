from collections import Counter


def print_bar_chart(data, mark):
    if type(data) is list:
        max_length = len(max(data, key=len))
    else:
        max_length = 1
    data = Counter(data)
    for k, v in sorted(data.items(), key=lambda x: x[1], reverse=True):
        print(f'{k.ljust(max_length)} |{mark * v}')
      
