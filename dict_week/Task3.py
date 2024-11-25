# Task3

country = {"America": "Washington", "UK": "London", "Uzbekistan": "Tashkent", "Russian": "Moscow", "China": "Pekin",
           "Japan": "Tokyo", "Korea": "Seoul"}
query = input('Qaysi davlatning poytaxtini bilishni istaysiz?:')
data = country.get(query, "-1")
if data != '-1':
    print(f"{query} ning poytaxti {data} ")
else:
    print("Kechirasiz bizda bunday davlat yo`q")
