# Task5
map = {"id": "10001", "password": "admin123", "name": "Admin"}
print("Before: ",map)
for k, v in map.items():
    if k == 'password':
        map[k] = f"{v}@"

print("After: ",map)