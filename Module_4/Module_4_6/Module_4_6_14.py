import pickle


def filter_dump(filename, objects, typename):
    with open(filename, 'wb') as file:
        lst = [i for i in objects if type(i) is typename]
        pickle.dump(lst, file)
        
