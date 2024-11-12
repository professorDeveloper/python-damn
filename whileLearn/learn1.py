# i = 1
# sum = 0
# while i <= 10:
#     i = i + 1
#     sum = sum + i
#
# # Task1
# i = 1
# while i <= 100:
#     if i % 2 == 0:
#         print(i)
#     i = i + 1
#
# # Task2
# i = 20
# while i <= 1000:
#     if i % 11 == 0:
#         print(i)
#     i = i + 1
#
# # Task3
# print("Task3 ")
# inputData = input("Enter a : ")
# while inputData != "stop":
#     print("Student Parolni to`g`ri kirit")
#     inputData = input("Enter  : ")

# Task4
i = 1
while i <= 2000:
    lastNum = i % 10
    if lastNum == 0:
        print(f"Oxiri 0 bilan tugaydigan son :{i}")
    i = i + 1

# Task5
sum = 0
i = -80
while i <100:
    i = i + 1
    if i % 5 == 0:
        sum = sum + i

print (f"5 ga bo`linadigan sonlar yig`indisi : {sum}")
# Task6
count = 0
i =1
while i <= 100:
    if i % 5 == 0:
        count = count + 1
    i = i + 1
print(f"1 dan 100gacha 5 ga bo`linadiganlar soni: {count}")