# Task1
num1 = int(input("Birinchi sonnni kiriting:"))
num2 = int(input("Ikkinchi sonni kiriting:"))

amal = int(input("1.Qoshish\n"
                 "2.Ko`paytirish\n"
                 "3.Ayrish\n"
                 "4.Bo`lish.  amalni tanlang :"))

if amal == 1:
    print(f"{num1} + {num2} = {num1 + num2}")
elif amal == 2:
    print(f"{num1} * {num2} = {num1 * num2}")
elif amal == 3:
    print(f"{num1}-{num2} = {num1 - num2}")
elif amal == 4:
    print(f"{num1} / {num2} = {num1 // num2}")
