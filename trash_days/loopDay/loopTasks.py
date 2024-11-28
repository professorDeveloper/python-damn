# Task3
counter = 0
for i in range(-80, 81):
    if i % 7 == 0:
        counter = counter + 1
print(f" 7 ga bolinuvchi sonlar soni :{counter} ")

# Task4
mevalar = ['olma', 'banan', 'apelsin', 'olma']
counter = 0
for meva in mevalar:
    if meva == 'olma':
        counter = counter + 1
print('Olma lar soni:', counter)

# Task 5
a = 2
b = 6
toqCount = 0
juftCount = 0
for i in range(a, b):
    if i % 2 == 0:
        juftCount += 1
    else:
        toqCount += 1
print("Toq:", toqCount)
print("Juft:", juftCount)

# Task6
x = [1, 2, 3, 4, 5, 6, 6, 8, 9]
counter = 0
for i in x:
    if i % 2 == 0:
        counter = counter + 1
print(f"2 ga bo`linadiganlar soni : {counter}")

# Task7
word = input("Enter a word:")
counter = 0
for i in word:
    if i.isupper():
        counter = counter + 1
# Task8

for i in range(1, 101):
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    else:
        print(i)
# Task9
dyums = [1, 2, 3, 4]
cmList = []
for i in dyums:
    cmList.append(i * 2.54)
# Task10
list = [5, 10, 15, 20, 25, 30]
newList = []
for i in list:
    if i > 10 and i % 2 == 0:
        newList.append(i)
# Task11
list = [5, 10, 15, 20, 25, 30]
newList = []
for i in list:
    newList.append(i % 3)

# Task12
x = ['olma', 'olxo`ri', 'banan', 'olcha']
for i in x:
    if i.startswith('o`'):
        print(i)
