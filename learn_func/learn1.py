# # Before Def task1
# import random
#
# sonlar = [1, 3, 4, 1, 66, 16, 71]
# for i in sonlar:
#     if i % 2 == 0:
#         print(i)
# # Before Def task2
# juftList = []
# for i in sonlar:
#     if i % 2 == 0:
#         juftList.append(i)
#
#
def thing():
    print("Hello World")
    print("Fun")


def thing2() -> str:
    return "Hello World"


thing()
a = thing2()

print(a)
