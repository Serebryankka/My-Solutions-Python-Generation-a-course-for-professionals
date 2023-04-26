from zipfile import ZipFile
from datetime import datetime


with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    sorted_info = sorted([(i.filename.split('/')[-1], i.date_time, i.file_size, i.compress_size) for i in info if not i.is_dir()])
    for i in sorted_info:
        print(f'''{i[0]}
  Дата модификации файла: {datetime.strftime(datetime(*i[1]), '%Y-%m-%d %H:%M:%S')}
  Объем исходного файла: {i[2]} байт(а)
  Объем сжатого файла: {i[3]} байт(а)''')
