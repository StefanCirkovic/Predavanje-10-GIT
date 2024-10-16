
import json

with open("data/user.json", 'r') as file:
    data = json.load(file)
    print(data[0]["name"])
    data.append({
        "name": "Petar Petrovic",
        "age": 31,
        "height": 190,
        "gender": "male"
    })

print(data)

with open("data/user.json", 'w') as file:
    json.dump(data, file, indent=4)
