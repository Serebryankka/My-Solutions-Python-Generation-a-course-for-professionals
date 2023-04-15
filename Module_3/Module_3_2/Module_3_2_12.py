from datetime import date


def main(data):
    data1, data2 = data
    return min(date.fromisoformat(data1), date.fromisoformat(data2)).strftime('%d-%m (%Y)')
print(main([input() for _ in range(2)])
  
