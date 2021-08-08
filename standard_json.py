import json
import csv

MAX_CALLS = 50

# process file
list_data = list()

next_file = "inputfiles\\file1.json"

for _ in range(MAX_CALLS):
    with open(next_file) as f:
        json_data = json.load(f)

    list_data += json_data['data']

    if json_data['meta']['next_file'] == "":
        break

    next_file = json_data['meta']['next_file']

with open('outputfiles\\animal_info.csv', 'w', newline='') as f:
    dw = csv.DictWriter(f, list_data[0].keys())
    dw.writeheader()
    dw.writerows(list_data)


