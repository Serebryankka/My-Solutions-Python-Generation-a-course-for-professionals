from zipfile import ZipFile


def extract_this(zip_name, *args):
    with ZipFile(zip_name) as zip_file:
        if not len(args):
            zip_file.extractall()
        else:
            for arg in args:
                zip_file.extract(arg)
                
