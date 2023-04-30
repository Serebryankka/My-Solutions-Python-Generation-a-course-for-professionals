import json


file_name = input()

try:
    with open(file_name, encoding='utf-8') as file:
        try:
            print(json.load(file))
        except json.decoder.JSONDecodeError:
            print('Ошибка при десериализации')
except FileNotFoundError:
    print('Файл не найден')
    
