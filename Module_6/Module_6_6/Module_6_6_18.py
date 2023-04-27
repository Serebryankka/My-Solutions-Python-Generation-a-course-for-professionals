from collections import OrderedDict


data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе',
                    'AdmArea': 'Центральный административный округ', 'District': 'район Арбат',
                    'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})

data_new = OrderedDict()
for i in range(len(data)):
    k, v = data.popitem(last=i%2)
    data_new.update({k: v})
print(data_new)
