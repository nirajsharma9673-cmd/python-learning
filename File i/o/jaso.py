import json

data = {
    "name": "Niraj",
    "age": 18,
    "branch": "IT"
}

with open("data.json", "w+") as f:
    json.dump(data, f)
