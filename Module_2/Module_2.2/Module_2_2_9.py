def main():
    def bytes(B=0, KB=0, MB=0, GB=0):
        B, KB, MB, GB = map(int, (B, KB, MB, GB))
        if GB != 0:
            MB += GB * 1024
        if MB != 0:
            KB += MB * 1024
        if KB != 0:
            B += KB * 1024
        count = 0
        while B >= 1024:
            B /= 1024
            count += 1
        d = {0: 'B', 1: 'KB', 2: 'MB', 3: 'GB'}
        return f'{round(B)} {d[count]}'

    with open('files.txt', 'r', encoding='utf-8') as f:
        d = {}
        for line in f:
            name, extension, size, unit = line.replace('.', ' ').split()
            d[extension] = d.get(extension, {'sizes': {unit: 0}, 'names': []})
            d[extension]['sizes'][unit] = d[extension]['sizes'].get(unit, 0) + int(size)
            d[extension]['names'] += [name]

    d = dict(sorted(d.items(), key=lambda x: x[0]))
    new_line = '\n'
    for ex in d:
        d[ex]['names'] = sorted(d[ex]['names'])
        print(f'''{f".{ex}{new_line}".join(d[ex]["names"])}.{ex}
----------
Summary: {bytes(**d[ex]['sizes'])}
    ''')


if __name__ == '__main__':
    main()
