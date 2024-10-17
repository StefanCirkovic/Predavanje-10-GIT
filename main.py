
from methods import load_file, save_file

# Učitaj podatke iz fajla
data = load_file("data/user.json")

# Prikaz podataka
print(data)

# Dodaj nove podatke
data.append({
    "name": "Test Test"
})

# Sačuvaj izmenjene podatke nazad u fajl
save_file("data/user.json", data)

