import math

info = {"Toshkent": "Uzbekistan", "Astana": "Kazak", "Washington": "AQSH", "Seoul": "Janubiy Korea"}
print(max(info.values(), key=lambda k: len(k)))

# Task2
a =max(info.items(), key=lambda k: len(k[1]))
print(a[0])
# Task3
print(sorted(info.values()))

#Task4
print(sorted(info.keys()))

# Task5
print(sorted(info.values(),key=len,reverse=True))
