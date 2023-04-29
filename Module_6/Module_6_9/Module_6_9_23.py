from collections import Counter
from collections import ChainMap

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

products = ChainMap(bread, meat, sauce, vegetables, toppings)
order = Counter(input().split(','))
max_length_word = len(max(order, key=len))
total = 0

for k, v in sorted(order.items()):
    print(f'{k.ljust(max_length_word)} x {v}')
    total += products[k] * v

total_str = f'ИТОГ: {total}р'
max_length_string = max((len(total_str), max_length_word + 3 + len(str(max(order.values())))))
print('-'.ljust(max_length_string, '-'))
print(total_str)
