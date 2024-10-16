
import json
from methods import load_file

data = load_file("products.json")
users = load_file("user.json")
print(data, users)
