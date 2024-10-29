ball = int(input("Enter a number: "))
if 0 < ball < 55:
    print("2 Qoniqarsiz")
elif 55 < ball < 71:
    print("3 Qoniqarli")
elif 71 < ball < 85:
    print("4 Yaxshi")
elif 85 < ball <= 100:
    print("5 A`lo")

#  Homework 2
# Elektromobilning 100 km masofani bosib o’tish uchun
# akkumlatoridagi to’liq quvvatning 40 foizini sarflaydi. Ayni
# paytda uning quvvati (energy) K foiz qolgan. Haydovchi D
# (distance) km masofaga borishi uchun quvvat yetarli yoki
# yetarli emasligini aniqlang. Agar bor quvvat yetarli bo’lmasa,
# yana necha foiz quvvat kerakligi (required power) ni aniqlang.
# Bunda K va D foydalanuvchi tomonidan kiritiladi
# Har 1 foiz 100 km / 40 ga teng bo'ladi.
# i.e = k=60 d=150   yetarli , 200  =yetarli emas yana 20 foiz quvvat kerak

k =int (input("Foizni kiriting: ")) # k=60
d = int(input("Masofani kiriting: ")) # D=150


powerPercent = (k*100)//40
if powerPercent >=d :
    print("Quvvat Yetarli")
else:
    ortiqchaMasofa =d-powerPercent # 100
    distanceToPercent =40*ortiqchaMasofa//100
    print(f"{distanceToPercent} % quvvat Yetarli emas Bu quvvat bilan {powerPercent}km gacha bo`lgan masofani bosib o`ta olasiz")

