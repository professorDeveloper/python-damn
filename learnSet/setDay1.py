# set1 = {1, 2, 3, 4, 4, 5, 6, 7, 8}
# print(set1)
# tuple1 = (1, 2, 3, 4, 4, 5, 6, 7, 8)
# setTup = set(tuple1)
# list1 = [1, 2, 3, 4, 4, 5, 6, 7, 8]
# print(list1[0:3])
# setList = set(list1)
# print(setTup)
# print(sorted(setTup))
#
# # setdan oxirgi elementni o`chirish
# set1.pop()


# setdan tanlangan elementni o`chirish
# set1.remove(4)
#
# # setdan barcha elementlarni ochirish
# set1.clear()

setExample = {1, 2, 3, 4, 5, 6, 6}
set2 = {3, 4, 5, 6, 8}
print(setExample.union(set2))
print(setExample.difference(set2))
print(setExample.intersection(set2))