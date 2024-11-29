import math
import random

info = {"Toshkent": "Uzbekistan", "Astana": "Kazak", "Washington": "AQSH", "Seoul": "Janubiy Korea"}
print(max(info.values(), key=lambda k: len(k)))

# Task2
a = max(info.items(), key=lambda k: len(k[1]))
print(a[0])
# Task3
print(sorted(info.values()))

# Task4
print(sorted(info.keys()))

# Task5
print(sorted(info.values(), key=len, reverse=True))

# Task6
students = ["Javlon", "Jamshid", "Husan", "Amirbek", "Olim"]
b = students[random.randint(0, len(students) - 1)]
print(b)
# Task7
while True:
    print("1-Student Imtihonga Chaqirish")
    print("2-Imtihonga kirmagan studentlar ro`yati")
    print("3->Dasturdan chqisih:")
    choice = int(input("Enter your choice: "))
    print()
    if choice == 1:
        if len(students) != 0:
            student = random.choice(students)
            print(f"Imtihonga Chaqiriladigan Tasodifiy odam {student}")
            students.remove(student, )
        else:
            print("Talabalar Qolmadi")
    elif choice == 2:
        print("====== Imtihonga kirmagan studentlar ro`yati ======")
        print(students)
        print("===================================================")
    elif choice == 3:
        print("Dasturdan Chiqildi !")
        break
    else:
        print("Invalid choice")
    print()
