# Task1
list_numbers = [1, 2, 3, 4, 5]
list_numbers[0] = 100
list_numbers.append(60)
print(len(list_numbers))

# Task2
fruits = ['apple', 'banana', 'cherry', 'apricot']
fruits[fruits.index('banana')] = 'mango'
fruits.append('orange')
fruits.append('kiwi')
fruits.sort()
print(fruits)

# Task3
students = ['Ali', 'Olim', 'Zarina', 'Jasur', 'Sabina']
print(students.index('Zarina'))
print(students[0])
print(students[-1])

# Task4
my_tuple = ("Ali", "Olim", "Zarina", "Jasur")
print(my_tuple[2])
print(len(my_tuple))

# Task5
my_tuple = (1, 2, 3,)
my_list = [1, 2, 3]
my_list[1] = 3
my_list.append(4)
print(my_list)
print(my_tuple)

# Python'da tuple — bu o'zgarmas (immutable) ma'lumotlar turidir . boshqa malumot turidan ham asosiy farqi shunda
# List mutable malumot turi va asosiy tuple va list dan farqi am shunda


# Task6
jobs = ('teachers', 'student', 'nurse')
jobs_list = list(jobs)
jobs_list.append('police')
jobs = tuple(jobs_list)
print(jobs)

# Task7
numbers = [10, 32, 50, 1]
numbers.reverse()
print(numbers)
tuple_nums = (1, 2, 3, 4, 5)
list_tuple = list(tuple_nums)
list_tuple.reverse()
tuple_nums = tuple(list_tuple)

# Task8
num_list = [1, 2, 3, 4]
num_tuple = (5, 6, 7, 8)
tuple_list = list(num_tuple)
num_list.extend(tuple_list)
num_list.sort()
print(f"Min {num_list[0]}")
print(f"Max {num_list[-1]}")

# Task9
fruits = ['apple', 'banana', 'cherry', 'apricot', 'fig']
fruits.remove('cherry')
fruits.pop()

# Task10
ages = [45, 32, 10, 25]
ages.sort()
print(ages)
ages = ages[::-1]
print(ages)

# Task11
nums = [12, 1, 2, 2, 3, 2, 4, 2, 2]
nums.sort()
lastIndex = nums.count(2)
nums = nums[lastIndex::]
print(nums[::-1])

# Task12
numbers_tuple =(10,50,25,5,100,75)
numbers_list =list(numbers_tuple)
numbers_list.sort()
numbers_tuple =numbers_list
print(numbers_tuple[0])
print(numbers_tuple[-1])
