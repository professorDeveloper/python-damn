# HomeTask1
fruits = ('apple', 'banana', 'cherry', 'tut')
fruitsList = list(fruits)
fruitsList.pop()
fruits = tuple(fruitsList)
print(fruits)

# HomeTask2
tuple_nums = (1, 2, 3, 4, 5, 11, -1, -16, 14, 3, 13)
nums_list = list(tuple_nums)
nums_list.sort()
nums_list.pop()
tuple_nums = tuple(nums_list)

# HomeTask3
tuple_nums = tuple(tuple_nums)
print(tuple_nums)
tuple_list = list(tuple_nums)
tuple_list.pop(3)
tuple_list.pop(4)
tuple_list.pop(5)
tuple_nums = tuple(tuple_list)
print(tuple_nums)

# HomeTask4
tuple_city = ('Toshkent', 'Buxoro', 'Samarqand', 'Namangna', 'Andijon', 'Jizzax')
list_city = list(tuple_city)
list_city.pop(2)
tuple_city = tuple(list_city)
print(tuple_city)

# HomeTask5
tuple_fruits = ('apple', 'strawberry', 'cherry', 'tut')
fruit_list = list(tuple_fruits)

fruit_list.sort(key=len)
tuple_fruits = tuple(fruit_list)
print(len(tuple_fruits[-1]))  # This Task Solved by GPT

# 2-Solution HomeTask5
leng_fruits = []
leng_fruits.append(len(fruit_list[0]))
leng_fruits.append(len(fruit_list[1]))
leng_fruits.append(len(fruit_list[2]))
leng_fruits.append(len(fruit_list[3]))
leng_fruits.sort()
print(leng_fruits[-1])
