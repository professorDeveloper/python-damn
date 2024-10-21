# Task1 Tuple
fruits = ('apple', 'banana', 'cherry', 'mango', 'orange', 'kiwi')
print(f"Last Item {fruits[-1]}")
print(f"First Item {fruits[0]}")
print(f"3rd Item {fruits[2]}")

# Tuple ga yangi tuple berish mumkin misol  my_tuple = new_tuple

# Task2 Tuple
colors = ('red', 'green', 'blue')
colors_list = list(colors)
colors_list.append('yellow')
colors = tuple(colors_list)
print(colors)

# Task3
letters_tuple = ('a', 'b', 'c', 'd', 'e')
tuple_list = list(letters_tuple)
tuple_list.reverse()
letters_tuple = tuple(tuple_list)
print(letters_tuple)

# Task4
my_tuple = (1, 2, 3, 4, 5)
tuple_list = list(my_tuple)
tuple_list.append(60)
my_tuple = tuple(tuple_list)

# Task5
tuple_list1 = (1, 2, 3)
tuple_list2 = (4, 5, 6)
list1 = list(tuple_list1)
list2 = list(tuple_list2)
list1.extend(list2)
extendTuple = tuple(list1)

print(extendTuple)
