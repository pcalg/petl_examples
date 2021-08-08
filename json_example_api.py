from typing import Optional
from fastapi import FastAPI
import json

app = FastAPI()

# test for paging (reuse the examples)
json_lookup = {
    "abcde500": "file2.json",
    "rtew3456": "file3.json"
}

@app.get("/")
def read_root():
    return {"Hello": "Pets"}


@app.get("/pets/")
def read_pets(q: Optional[str] = None):

    if (q == None):
        pet_file = "file1.json"
    else:
        pet_file = json_lookup[q]

    with open("inputfiles/" + pet_file, 'r') as f:
        json_data = json.load(f)

    return json_data
