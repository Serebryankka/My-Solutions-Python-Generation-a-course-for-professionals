import string


x = string.ascii_lowercase
y = input()
str = input().lower()
tbl = str.maketrans(x, y)
print(str.translate(tbl))
