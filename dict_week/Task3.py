# Task3

country = {"America": "Washington", "UK": "London", "Uzbekistan": "Tashkent", "Russian": "Moscow", "China": "Pekin",
           "Japan": "Tokyo", "Korea": "Seoul"}
query = input('Qaysi davlatning poytaxtini bilishni istaysiz?:')
data = country.get(query, "false")

if data != 'false':
    print(f"{query} ning poytaxti {data} ")
else:
    print("Kechirasiz bizda bunday davlat yo`q")
# Task3 Done