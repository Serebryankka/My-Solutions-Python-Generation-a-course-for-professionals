data = eval(input())

if isinstance(data,list):
    print(data[-1])
elif isinstance(data, tuple):
    print(data[0])
elif isinstance(data, set):
    print(len(data))
