from datetime import datetime, timedelta


def main(data):
    total = 0
    for i in data:
        total += (datetime.strptime(i[1], '%H:%M') - datetime.strptime(i[0], '%H:%M')).seconds // 60
    return total

if __name__ == '__main__':
    print(main(data=[('07:14', '08:46'),

('09:01', '09:37'),

('10:00', '11:43'),

('12:13', '13:49'),

('15:00', '15:19'),

('15:58', '17:24'),

('17:57', '19:21'),

('19:30', '19:59')]))
    
