# Task5
map = {"id": "10001", "password": "admin12@3", "name": "Admin"}
print("Before: ",map)
for k, v in map.items():
    if k == 'password' and v.find('@') == -1:
        map[k] = f"{v}@"

print("After: ",map)