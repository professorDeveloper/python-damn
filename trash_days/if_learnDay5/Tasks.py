# Task1
num = int(input("Enter a number: "))
if num > 0:
    num += 1
    print(f"You entered {num}")

# Task2
num = int(input("Enter a number: "))
if num > 0:
    num += 1
else:
    num -= 2

print(f"num -> {num}")

# Task3
num = int(input("Enter a number: "))

if num > 0:
    num += 1
elif num == 0:
    num = 10
else:
    num -= 2
print(f"num -> {num}")

# Task4
num = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
count = 0
if num > 0: count += 1
if num2 > 0: count += 1
if num3 > 0: count += 1
print(f"Musbatlar soni :{count}")

# Task5
num = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
countMusbat = 0
countManfiy = 0
if num > 0:
    countMusbat += 1
else:
    countManfiy += 1
if num2 > 0:
    countMusbat += 1
else:
    countManfiy += 1
if num3 > 0:
    countMusbat += 1
else:
    countManfiy += 1
print(f"Musbatlar soni :{countMusbat}")
print(f"Manfiylar soni :{countManfiy}")

# task6
num = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
maxNum = num
if num2 > maxNum:
    maxNum = num2
print(f"Max numm {maxNum}")

# task7
num = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
index = 1
if num2 > num:
    index = 2
else:
    index = 1
print(f"Index: {index}")

# task8
num = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

if num2 > num:
    print(f"{num2} > {num}")
else:
    print(f"{num} > {num2}")

# Task9

a = float(input("Enter a number: "))
b = float(input("Enter a number: "))

if a > b:
    temp = a
    a = b
    b = temp
    print(f"{a} > {b}")
else:
    print(f"{a} > {b}")

# Task10

num = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
if num == num2:
    num = 0
    num2 = 0
else:
    total = num2 + num
    num = total
    num2 = total

print(f"a = {num} < b= {num2}")

# task11
num = int(input("Enter num:"))
num2 = int(input("Enter num2:"))
if num == num2:
    num = 0
    num2 = 0
else:
    max = num
    if num < num2:
        max = num2
    num = max
    num2 = max
print(f"num1 -> {num} , num2 -> {num2}")

# task12
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
min = 0
if num2 < num1 and num2 < num3:
    min = num2
elif num3 < num1 and num3 < num2:
    min = num3
elif num1 < num2 and num1 < num3:
    min = num1

print(f"Min num {min}")

# Task13
num = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
middleNum = 0
if num2 > num3 > num1:
    middleNum = num3
elif num1 > num3 > num2:
    middleNum = num3
elif num3 > num2 > num1:
    middleNum = num2
elif num1 > num2 > num3:
    middleNum = num2
elif num2 > num1 > num3:
    middleNum = num1
elif num3 > num1 > num2:
    middleNum = num1
print(f"Middle num {middleNum}")

# Task14

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
min = 0
if num2 < num1 and num2 < num3:
    min = num2
elif num3 < num1 and num3 < num2:
    min = num3
elif num1 < num2 and num1 < num3:
    min = num1

max = 0
if num2 > num1 and num2 > num3:
    max = num2
elif num3 > num1 and num3 > num2:
    max = num3
elif num1 > num3 and num1 > num2:
    max = num1
print(f" Max num : {max} Min num : {min}")

# Task15
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
firstN = 0
secondNum = 0
if num1 + num2 > num3 + num2 and num1 + num2 > num1 + num3:
    firstN = num1
    secondNum = num2
elif num1 + num3 > num3 + num2 and num2 + num1:
    firstN = num1
    secondNum = num2
elif num2 + num3 > num1 + num2 and num1 + num3:
    firstN = num2
    secondNum = num3

print(f"first Num :{firstN} second num : {secondNum}")

# Task16
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

if num1 < num2 < num3:
    num1 *= 2
    num2 *= 2
    num3 *= 2
else:
    num1 = -num1
    num2 = -num2
    num3 = -num3

print(f"a: {num1} b= {num2} c={num3} ")

# task17

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

if num1 < num2 < num3 or num1 > num2 > num3:
    num1 *= 2
    num2 *= 2
    num3 *= 2
else:
    num1 = -num1
    num2 = -num2
    num3 = -num3

print(f"a: {num1} b= {num2} c={num3} ")
