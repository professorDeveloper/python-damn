import math
import random

# Modulega o`tkazish
num = int(input("Enter a number: "))
print(f"Kiritilgan Son:{num} Natija -> {abs(num)}")

# Dars2 Yaxlitlash
son = float(input("Enter a number: "))
print(f"Kiritilgan Son: {son} Natija -> {round(son, 2)}")

# Task3
print(f"Kiritilgan Son: {num} Kvadrat: {pow(num, 2)}  Kub: {pow(num, 3)}")

# Random
randomNumber = random.randint(1, 100)
print(f"Random num : {randomNumber}")

# Random Element from list
listD = [2, 3, 4, 15, 66, 12]
randomIndex = random.choice(listD)
print(f"Random Element : {randomIndex}")

# Random Game
isOver = False
heart = 5
randomNum = random.randint(1, 50)
print("O`yinga xush kelibsiz 1 dan 50 gacha bo`lgan son kiriting :")
while not isOver:
    userNum = int(input("Enter a number: "))
    if userNum != randomNum:
        if heart > 0:
            if userNum > randomNum:
                heart -= 1
                print("siz kiritgan son kattaroq")
                print(f"Urunishlar soni : {heart}")
            else:
                heart -=1
                print("siz kiritgan son kichikroq")
                print(f"Urunishlar : {heart}")
        else:
            print("Game Over urunishlar qolmadi")
            isOver = True
    else:
        isOver=True
        print("You`re Win !")