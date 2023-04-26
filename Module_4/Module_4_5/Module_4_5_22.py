from zipfile import ZipFile
import json


result = []

with ZipFile('data.zip') as zip_file:
    for file in zip_file.infolist():
        if file.filename.endswith('.json'):
            with zip_file.open(file.filename) as f:
                try:
                    data = json.loads(f.read().decode('utf-8'))
                    if data['team'] == 'Arsenal':
                        result.append(f'{data["first_name"]} {data["last_name"]}')
                except (json.decoder.JSONDecodeError, UnicodeDecodeError):
                    continue
                    
print(*sorted(result), sep='\n')
