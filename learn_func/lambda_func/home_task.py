# Task1
son_qosh = lambda a, b: a + b
print(son_qosh(2, 2))

# Task2
new_list = [2, 3, 14, 55, 15, 21, 15, 13, 21]
juft_list = list(filter(lambda x: x % 2 == 0, new_list))
print(juft_list)

# Task3
sorted_list = list(filter(lambda x: x > 10, new_list))
print(sorted_list)

# Task4
kvadratAniqlash = lambda a: a * a
print(kvadratAniqlash(2))
# Task5
names = ["alice", "bob", "charlie", "david", "eve", "anna", "alex"]

sorted_names = list(filter(lambda x: str(x).lower().startswith('a'), names))

print(sorted_names)

# Task6
price_tax = lambda price: price * 0.10
print(price_tax(100), " soliq ")

# Task7
list1 = list(map(lambda x: str(x)[0].upper(), names))
print(list1)

# Task8
plus = lambda a, b: a + b
minus = lambda a, b: a - b
kopaytrsh = lambda a, b: a * b
bolish = lambda a, b: a // b
print(kopaytrsh(100, 100))
print(bolish(100, 100))
print(min(120, 100))
print(plus(100, 10))

# Task 9
# I don`t understand that :(


# Task10
new_list = [2, 3, 14, 55, 15, 21, 15, 13, 21]
list2 = list(filter(lambda x: x > 50, new_list))
print(list2)

# Task11
word = "Hello World in Python"
checkWord = lambda word: True if str(word).find("Python") != -1 else False
print(checkWord(word))

# Task12
tempratures = [32, 35, 37, 40, 41, 42, 43, 44, 45]

farangyte_tempratures = list(map(lambda x: (x * 9 / 5) + 32, tempratures))
print(farangyte_tempratures)

# Task13
findLength = lambda x: sorted(list(x), key=lambda x: len(x), reverse=True)[0]
print(findLength(names))


# Task14
filtered_list = list(filter(lambda x: x % 2 == 0 and x > 5, tempratures))
print(filtered_list)


