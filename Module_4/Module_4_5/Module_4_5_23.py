from zipfile import ZipFile


def convert(n):
    unit = ['B', 'KB', 'MB', 'GB']
    step = 0
    while 1024 < n:
        n /= 1024
        step += 1
    return round(n), unit[step]

with ZipFile('desktop.zip') as zip_file:
    for file in zip_file.infolist():
        filename = file.filename.rstrip('/').split('/')
        filename_len = len(filename)
        if file.is_dir() and filename_len == 1:
            print(*filename)
        else:
            s = str()
            for i in range(filename_len-1):
                s += '  '
            print(f'{s}{filename[-1]}', *convert(file.file_size))
