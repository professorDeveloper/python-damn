# # Task1
# sum = 0
# number = int(input("Enter a number: "))
# while number != 0:
#     sum = sum + number
#     number = int(input("Enter a number: "))
# print(f"Sum :{sum}")
#
# # Task2
# a = 2
# b = 10
# sum = 0
# i = a
# while i <= b:
#     sum = sum + i
#     i = i + 1
#
# # Task3
# numbers = []
# num = int(input("Raqamlar soni: "))
# i = 0
# while i < num:
#     number = int(input("Raqam: "))
#     numbers.append(number)
#     i = i + 1
# # Task4
# x = [12, 3, 4, 5, 6, 6, 7, 8]
# max = x[0]
# i = 0
# while i < len(x):
#     if x[i] > max:
#         max = x[i]
#     i = i + 1
# print("Eng Katta element:", max)
#
# # Task5
# x = [1, 2, 3, 4, 566, 13]
# maxIndex = 0
# max = x[0]
# i = 0
# while i < len(x):
#     if x[i] > max:
#         max = x[i]
#         maxIndex = i
#     i = i + 1
# print(f"Eng Katta element:{max} index:{maxIndex}")
#
# # Task6
# num = 1
# count = 0
# while num != 0:
#     num = num // 10
#     count += 1
#
# print(count)
#
# # Task7
# x = [1, 2, 3, 4, 566, 13]
# maxElement = x[0]
# minElement = x[0]
# i = 0
# while i < len(x):
#     if x[i] > maxElement:
#         maxElement = x[i]
#     if x[i] < minElement:
#         minElement = x[i]
#     i = i + 1
# print("Eng Katta element:", maxElement)
# print("Eng Kichik element:", minElement)
#
# # Task8
# x = [1, 2, 3, 4, 566, 13]
# i = 0
# maxElement = x[0]
# minElement = x[0]
# maxIndex = 0
# minIndex = 0
# while i < len(x):
#     if x[i] > maxElement:
#         maxElement = x[i]
#         maxIndex = i
#     if x[i] < minElement:
#         minElement = x[i]
#         minIndex = i
#     i = i + 1
# # O`rin almashtirish
# temp = x[maxIndex]
# x[maxIndex] = x[minIndex]
# x[minIndex] = temp
#
# # Task9
# x = [1, 2, 3, 4, 566, 13]
# count = 0
# i = 0
# num = input("Number: ")
# while i < len(x) or count == 0:
#     if num == x[i]:
#         count = count + 1
#     i = i + 1
#
# if count == 0:
#     print("Raqam list ichida mavjud emas")
# else:
#     print("Raqam list ichida mavjud !")
#
# ##EKUB
# # Task 10
# a = 40
# b = 10
# while b != 0:
#     t = b
#     b = a % b
#     a = t
#
# print(f"Ekub {a} , {b} = {a}")
#
# # EKUK Task 11
#
# # while do
#
# # FL task
# user_num = 1
# a = 0
# while user_num != 0:
#     user_num = int(input("Enter a number: "))
#     a = a + user_num
# print(f"Siz kiritgan sonlar yig`indisi :{a}")
#
# # # Task1
# stop = ""
#
# while stop != 'stop':
#     print("Dasturni to'xtatish uchun stop ni yozing")
#     stop = input("Matn:")
#
# # Task2
# num = 1
# while num != 0:
#     num = int(input("Son kiriting:"))
#
#     if num != 0:
#         if num % 2 == 0:
#             print("Siz juft son kiritdingiz")
#         else:
#             print("Siz toqson kiritdingiz")
#
# # Tas3
# juftSonlar = []
# toqSonlar = []
# isStop = False
# while not isStop:
#     num = input("Raqam kiriting:")
#     if num == 'stop':
#         isStop = True
#     elif num.isdigit() or (num[0] == '-' and num[1:].isdigit()):
#         if int(num) % 2 == 0:
#             juftSonlar.append(int(num))
#         else:
#             toqSonlar.append(int(num))
# print(juftSonlar)
# print(toqSonlar)
#
#

#
# # Learn Break &&
# for i in range(1, 11):
#     if i == 5:
#         print("5 topildi, sikl to`xtatildi.")
#         break
#     print(i)
#
# # Task1
#
# for i in range(1, 11):
#     if i % 2 != 0:
#         print("5 topildi, sikl to`xtatildi.")
#         break
#     print(i)


# EKUB
# Task 10
# a = 45
# b = 63
# while b != 0:
#     t = b
#     b = a % b
#     a = t
#
# print(f"Ekub {a}")

# ekub with while
a = 45
b = 53
i = 1
ekub = 1
while i <= a:
    if a % i == 0 and b % i == 0:
        ekub = ekub + 1
    ekub = i
    i = i + 1
print(f"Ekub with while {ekub}")

# EkUB with for
a = int(input("Enter a: "))
b = int(input("Enter b: "))
if a > b:
    a, b = b, a
ekub = 1
for i in range(1, a + 1):
    if a % i == 0 and b % i == 0:
        ekub = ekub
print(f"EKUB is {ekub}")

# Ekuk with for idk why FOR
c = b
ekuk = b
for _ in range(1, a * b):
    if c % a == 0 and c % b == 0:
        ekuk = c
        break
    c = c + 1
print(f"EKUK is {ekuk}")

# Tub Son
number = int(input("1 dan Nechigacha bo`lgan chegarani kiriting: "))  # 3
for j in range(1, number + 1):
    count = 0  #
    for i in range(1, j + 1):
        if j % i == 0:
            count += 1
    if count == 2:
        print(f"{j} -> tub son")
    else:
        print(f"{j} -> tub son emas")
