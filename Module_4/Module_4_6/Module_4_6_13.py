import pickle
import sys


with open(input(), mode='rb') as file:
    fnc = pickle.load(file)
    print(fnc(*[line.rstrip() for line in sys.stdin]))
    
