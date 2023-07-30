import csv

import io
import csv

def dedup(new_data, old_data):
    unique_rows = set()
    new_reader = csv.reader(io.StringIO(new_data), skipinitialspace=True)
    old_reader = csv.reader(io.StringIO(old_data), skipinitialspace=True)

    for row in new_reader:
        unique_rows.add(tuple(row))
    for row in old_reader:
        unique_rows.add(tuple(row))

    sorted_tuple = tuple(sorted(unique_rows))
    tumple_to_str = ""
    for row in sorted_tuple:
        for item in row:
            if item == row[0]:
                tumple_to_str += "\"" + item + "\", "
            elif item == row[1]:
                tumple_to_str += "\"" + item + "\""
        tumple_to_str += "\n"
    return tumple_to_str

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
