# Task5
map = {"id": "10001", "password": "admin12@3", "name": "Admin"}
print("Before: ", map)
for k, v in map.items():
    if k == 'password' and v.find('@') == -1:  # agar mavjud bo`lsa bu shart emas )
        map[k] = f"{v}@"
        break

print("After: ", map)
# Task5 Updated