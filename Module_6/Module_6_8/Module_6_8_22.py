from collections import Counter


def main():
    books = Counter(input().split())
    total = 0
    for _ in range(int(input())):
        _class, price = input().split()
        if books[_class] > 0:
            books[_class] -= 1
            total += int(price)

    return total
  
  
if __name__ == '__main__':
    print(main())
    
