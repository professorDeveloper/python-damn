# Task1
num1 = float(input("number1: "))
num2 = float(input("number2: "))  # int = 2 float =2.3
if num1 < 0 or num2 < 0:
    print(True)

# Task2
if (num1 < 0 < num2) or (num1 > 0       > num2):
    print(True)  # - +   yoki + -

# Task2 Rewrite Clean Code
num1 = float(input("number1: "))
num2 = float(input("number2: "))
check = num1 * num2 > 0
if check:
    print(True)

# Task3
number = int(input("number: "))
if 9 < number < 100:
    print(True)
# Task4
number3Xonali = int(input("number3: "))  # 123  = 1 ,  2, 3
birlar = number3Xonali % 10
onlar = number3Xonali // 10 % 10
yuzlar = number3Xonali // 100 % 10
print(f"birlar : {birlar},onlar:{onlar},yuzlar:{yuzlar}")

if birlar != onlar and onlar != yuzlar:
    print(True)

# Task5
num = int(input("number: "))
if 1000 <= num < 9999:
    if num % 2 == 0:
        print(f"{num} is Juft")
    else:
        print(f"{num} is Toq")

# Task6
width = int(input("width: "))
height = int(input("height: "))
if width == height:
    print("Bu kvadrat")
else:
    print("oddiy to'rtburchak.")

# Task 7
num1 = float(input("number1: "))
num2 = float(input("number2: "))

if num1 > num2:
    print(f"{num1}  katta {num2} dan")
else:
    print(f"{num2}  katta {num1} dan")
