import csv
import json

def transform_csv_to_json(csv_file):
    json_data = {}

    with open(csv_file) as csvfile:
        reader = csv.reader(csvfile, quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
        for row in reader:
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

# Input CSV file path
csv_file = 'prizelist.csv'

json_data = transform_csv_to_json(csv_file)

# Convert dictionary to pretty-printed JSON string
json_str = json.dumps(json_data, indent=2)

# Output JSON to a file (optional)
output_file = 'output.json'
with open(output_file, 'w') as jsonfile:
    jsonfile.write(json_str)

# Print JSON string (optional)
print(json_str)
