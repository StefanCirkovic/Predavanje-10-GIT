
from methods import load_file, save_file

data = load_file("user.json")

print(data)

data.append({
    "name": "Test Test"
})

save_file("user.json", data)

#with open("data.json", 'w') as file:
#    json.dump(data, file, indent=4)

