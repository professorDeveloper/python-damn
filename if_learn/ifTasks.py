age = int(input("Enter your age:"))

if age >= 18:
    print("Xush kelibsiz")
else:
    print("Hozirda dasturdan foydalana olmaysiz !")

# Task2
login = input("Loginni kiriting:")
password = input("Parolni kiriting:")
if password == 'admin' and login == '12345678':
    print("Dasturga xush kelibsiz")
else:
    print("Parol yoki Login Xato !")

# Task1
number = int(input("Enter N:"))
if number >= 0:
    print(number + 1)
else:
    print(number)
# Task 2
num1 = int(input("Enter N:"))
num2 = int(input("Enter N:"))
num3 = int(input("Enter N:"))
if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
else:
    print(num3)
# Task4
number = int(input("Enter N:"))

if number % 2 == 0:
    print("Juft son")
else:
    print("Toq son")
