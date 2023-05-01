def func(n):
    if n != 0:
        func(int(input()))
        print(n)
    else:
        print(0)
        
        
func(int(input()))
