obhavo = input("bugun qanday obhavo=")
if obhavo == "quyoshli":
    print("Yengilroq kiyining")
elif obhavo == "qorli":
    print("Qalinroq kiyining")
elif obhavo == "yomg`irli":
    print("Soyabon oling")
else:
    print("Xato malumot kiritildi !")

# Task2
num = int(input("Enter a number: "))
if num == 1:
    print("Dushanba")
elif num == 2:
    print("Seshanba")
elif num == 3:
    print("Chorshanba")
elif num == 4:
    print("Payshanba")
elif num == 5:
    print("Juma")
elif num == 6:
    print("Shanba")
elif num == 7:
    print("Yakshanba")
else:
    print("Xato son kiritildi !")

# if04
num = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter another number: "))
count = 0
if num > 0:
    count += 1
if num2 > 0:
    count += 1
if 0 < num3:
    count += 1
print(f"Natija :{count}")

# ifMonth
month = int(input("Enter a month: "))
if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("Aprill")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("Nowemmber")
elif month == 12:
    print("December")
else:
    print("Invalid month ! :(")
