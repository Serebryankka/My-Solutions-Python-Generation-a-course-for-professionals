def is_good_password(string):
    if len(string) >= 9:
        low, up, dig = 0, 0, 0
        for s in string:
            if s.isdigit():
                dig += 1
            elif s.islower():
                low += 1
            elif s.isupper():
                up += 1
        return all((low, up, dig))
    return False
    
