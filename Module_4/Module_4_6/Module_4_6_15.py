import pickle


def get_sum(obj):
    numbers = [i for i in obj if type(i) is int]
    if not numbers:
        return 0
    if type(obj) is list:
        return min(numbers) * max(numbers)
    elif type(obj) is dict:
        return sum(numbers)


if __name__ == '__main__':
    filename = input()
    num = int(input())

    with open(filename, 'rb') as file:
        obj = pickle.load(file)

    if num == get_sum(obj):
        print('Контрольные суммы совпадают')
    else:
        print('Контрольные суммы не совпадают')
        
