class LengthError(Exception):
    pass


class LetterError(Exception):
    pass


class DigitError(Exception):
    pass


def is_good_password(string):
    if len(string) < 9:
        raise LengthError
    low, up, dig = 0, 0, 0
    for s in string:
        if s.isdigit():
            dig += 1
        elif s.islower():
            low += 1
        elif s.isupper():
            up += 1
    if not low or not up:
        raise LetterError
    elif not dig:
        raise DigitError
    return True
    
