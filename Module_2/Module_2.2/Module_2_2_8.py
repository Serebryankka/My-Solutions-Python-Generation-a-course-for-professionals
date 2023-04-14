def task():
    emails = list(map(lambda x: x.rstrip('@beegeek.bzz'), (input() for _ in range(int(input())))))
    names = (input() for _ in range(int(input())))
    new_emails = []
    for name in names:
        email = name
        count = 0
        while email in emails or email in new_emails:
            count += 1
            email = name + str(count)
        new_emails.append(email)
    return '@beegeek.bzz\n'.join(new_emails) + '@beegeek.bzz'


if __name__ == '__main__':
    print(task())
    
