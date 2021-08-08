import json
import csv
import requests

MAX_PAGES = 100

def format_url(page = ""):
    if page == "":
        return "http://127.0.0.1:8000/pets/"
    else:
        return f"http://127.0.0.1:8000/pets?q={page}"

def get_pet_data():
    pet_data = list()
    next_page = ""

    for page_count in range(MAX_PAGES):
        r = requests.get(format_url(next_page))
        r.raise_for_status()

        print(r.text)

        json_data = r.json()

        pet_data += json_data['data']

        next_page = json_data['meta']['next_page']

        # no more pages
        if next_page == "":
            break

        # check if there are even more records
        if page_count == MAX_PAGES - 1 and next_page != "":
            raise Exception("More pages than expected")

    return pet_data

list_data = get_pet_data()

with open('outputfiles\\animal_info.csv', 'w', newline='') as f:
    dw = csv.DictWriter(f, list_data[0].keys())
    dw.writeheader()
    dw.writerows(list_data)


