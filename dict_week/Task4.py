# Task4
menu = {
    "osh": 20000,
    "non": 4000,
    "sho'rva": 15000,
    "kabob": 30000,
    "lag'mon": 18000,
    "manti": 25000,
    "somsa": 7000,
    "choy": 2000,
    "shashlik": 15000,
    "salat": 10000
}
max_foods = int(input("Buyrtmalar Soni:"))
buyurtmalar = []

while len(buyurtmalar) < max_foods:
    taom = input(f"{len(buyurtmalar) + 1}-taomni kiriting: ").lower()
    buyurtmalar.append(taom)

for taom in buyurtmalar:
    if taom in menu:
        print(f"{taom} - {menu[taom]} so`m")
    else:
        print(f"Kechirasiz, Bizda {taom}  yo`q.")

# I like this project :)
# Good Task, For Learn
