# Task1
sum = 0
number = int(input("Enter a number: "))
while number != 0:
    sum = sum + number
    number = int(input("Enter a number: "))
print(f"Sum :{sum}")

# Task2
a = 2
b = 10
sum = 0
i = a
while i <= b:
    sum = sum + i
    i = i + 1

# Task3
numbers = []
num = int(input("Raqamlar soni: "))
i = 0
while i < num:
    number = int(input("Raqam: "))
    numbers.append(number)
    i = i + 1
# Task4
x = [12, 3, 4, 5, 6, 6, 7, 8]
max = x[0]
i = 0
while i < len(x):
    if x[i] > max:
        max = x[i]
    i = i + 1
print("Eng Katta element:", max)

# Task5
x = [1, 2, 3, 4, 566, 13]
maxIndex = 0
max = x[0]
i = 0
while i < len(x):
    if x[i] > max:
        max = x[i]
        maxIndex = i
    i = i + 1
print(f"Eng Katta element:{max} index:{maxIndex}")

# Task6
num = 1
count = 0
while num != 0:
    num = num // 10
    count += 1

print(count)

# Task7
x = [1, 2, 3, 4, 566, 13]
maxElement = x[0]
minElement = x[0]
i = 0
while i < len(x):
    if x[i] > maxElement:
        maxElement = x[i]
    if x[i] < minElement:
        minElement = x[i]
    i = i + 1
print("Eng Katta element:", maxElement)
print("Eng Kichik element:", minElement)

# Task8
x = [1, 2, 3, 4, 566, 13]
i = 0
maxElement = x[0]
minElement = x[0]
maxIndex = 0
minIndex = 0
while i < len(x):
    if x[i] > maxElement:
        maxElement = x[i]
        maxIndex = i
    if x[i] < minElement:
        minElement = x[i]
        minIndex = i
    i = i + 1
# O`rin almashtirish
temp = x[maxIndex]
x[maxIndex] = x[minIndex]
x[minIndex] = temp

# Task9
x = [1, 2, 3, 4, 566, 13]
count = 0
i = 0
num = input("Number: ")
while i < len(x) or count == 0:
    if num == x[i]:
        count = count + 1
    i = i + 1

if count == 0:
    print("Raqam list ichida mavjud emas")
else:
    print("Raqam list ichida mavjud !")

# Task 10
# Ekub ni aniqlash
# while (b != 0) {
# int t = b;
# b = a % b;
# a = t;
# }
a =4
b=10
while b!=0:
    t=b
    b=a%b
    a=t

print(f"Ekub {a} , {b} = {a}")

# EKUK Task 11