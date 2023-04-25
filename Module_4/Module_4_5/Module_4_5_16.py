from zipfile import ZipFile


with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    min_val = 1
    for i in info:
        try:
            if (i.compress_size/i.file_size) < min_val:
                min_val = i.compress_size/i.file_size
                file_name = i.filename
        except ZeroDivisionError:
            continue
    print(file_name.split('/')[-1])
    
