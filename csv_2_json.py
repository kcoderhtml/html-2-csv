import csv

import io
import csv

def transform_csv_to_json(csv_file):
    json_data = {}
    print(csv_file)
    reader = csv.reader(io.StringIO(csv_file), skipinitialspace=True)
    for row in reader:
        print(row)
        if len(row) < 2:
            print(f"Invalid row format: {row}. Skipping...")
            continue
        names = row[0]
        event = row[1]
        names = names.split(', ')
        
        if len(names) < 2:
            print(f"Invalid name format: {names}. Skipping...")
            print(f"Event: {event}")
            continue
        
        family_name = names[0]
        first_name = names[1].split(' ')[0]

        if 'family' not in json_data:
            json_data['family'] = {}
        
        if family_name not in json_data['family']:
            json_data['family'][family_name] = {}
        
        if first_name not in json_data['family'][family_name]:
            json_data['family'][family_name][first_name] = []
        
        json_data['family'][family_name][first_name].append(event.strip())

    return json_data
