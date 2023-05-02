def func(number):
    if 0 < number:
        print(number)
        func(number - 5)
    print(number)
    
if __name__ == '__main__':    
    func(int(input())
         
