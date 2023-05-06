def verification(login, password, success, failure):
    letter, up, low, digit = 0, 0, 0, 0
    for s in password:
        if s.isalpha() and s.isascii():
            letter += 1
            if s.isupper():
                up += 1
            else:
                low += 1
        elif s.isdigit():
            digit += 1
    if not letter:
        failure(login, 'в пароле нет ни одной буквы')
    elif not up:
        failure(login, 'в пароле нет ни одной заглавной буквы')
    elif not low:
        failure(login, 'в пароле нет ни одной строчной буквы')
    elif not digit:
        failure(login, 'в пароле нет ни одной цифры')
    else:
        success(login)
