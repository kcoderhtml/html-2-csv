import soup_parser, csv_2_json
import json

def save_to_file(file_name, data):
    print(data)
    if (input("save to file Y/N: ").lower() == "y"):
        with open(file_name, "w") as f:
            f.write(data)
        print("saving...")
        print("saved to " + file_name)
    else:
        print("quitting...")
        exit()

# Input CSV file path
indicator = "                            &nbsp;&nbsp;&nbsp;&nbsp;"
# file name variables
html_path = "prizelists/html/prizelist-2023-08-30.html"
data_path = "prizelists/data/prizelist-2023-08-30"

# get lines containing inficator then deduplicate and format to csv
relevant_lines = soup_parser.dump_relevant_lines(html_path, indicator)
csv_coverted = soup_parser.convert_to_csv(relevant_lines)
deduped = soup_parser.dedup(csv_coverted)
csv = soup_parser.array_to_str(deduped)

# print csv data and check if its okay to write to file
save_to_file(data_path + ".csv", csv)

json_data = csv_2_json.transform_csv_to_json(csv)

# Convert dictionary to pretty-printed JSON string
json_str = json.dumps(json_data, indent=2)

# Output JSON to a file (optional)
save_to_file(data_path + ".json", json_str)