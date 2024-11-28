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
