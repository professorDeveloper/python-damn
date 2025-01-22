# def abc(a, b, c):
#     return a + b + c
#
#
# # positional argument berish
# print(abc(1, 2, 3))
#
# # named argument berish
#
# print(abc(b=12, c=10, a=4))
#
#
# # Funksiyani hardoim positional chaqirish
# def add(a: int, b: int, /) -> int:
#     return a + b
#
#
# # Funksiyani har doim named qilib chaqirish
# def addWithoutPos(*, a, b) -> int:
#     return a + b
#
#
# # c = add(b=20, a=10) ## Funksiyani hardoim positional chaqirish
# # c = addWithoutPos(a=20, b=10)  ## Funksiyani har doim named qilib chaqirish
# # print(c)
#
#
# def multipleProcess(*, a: int,  b: int) -> int:
#     return a * b
#
#
# print(multipleProcess(a=1, b=10))
#
#
#
# ##  Istalgancha sonlar qabul qilib ularning ko`paytmasini hisoblab beruvchi funksiya yozing
#
# def sonKopyatirish(*args):
#     sum =1
#     for item in args: # 2,3
#         sum*=item # 2 ,6
#     print(sum)
#
# sonKopyatirish(
#  2,3,4
# )
#
#
#
#
