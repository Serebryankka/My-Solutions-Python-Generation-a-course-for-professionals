import sys


class PasswordError(Exception): pass
    

class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


def is_good_password(string):
    if len(string) < 9:
        raise LengthError('LengthError')
    low, up, dig = 0, 0, 0
    for s in string:
        if s.isdigit():
            dig += 1
        elif s.islower():
            low += 1
        elif s.isupper():
            up += 1
    if not low or not up:
        raise LetterError('LetterError')
    elif not dig:
        raise DigitError('DigitError')
    return True


for line in sys.stdin:
    try:
        is_good_password(line.rstrip())
        print('Success!')
        break
    except PasswordError as err:
        print(err)
        
