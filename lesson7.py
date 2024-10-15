import math

name = "Azamov"

name = name.upper()  ## AZAMOV

print(name)

# Task1

num1 = int(input("Enter a number: "))
num2 = int(input("Enter b number: "))
result = num1 - num2
print(f"Task1 : Ayirma{result}")

# task2
isBigFirst = num1 > num2  ## > <
print(f"Task2 Birinchi son ikkinchisidan kattami ?{isBigFirst}")

# task3

isBigSecond = num1 <= num2
print(f"Task3 Ikkinchi son Birinchisidan kattami yoki teng ?{isBigSecond}")

# task 4

resNum = num1 / num2
print(f"Task4 birinchi sonni 2-sonnga bo`linma :{resNum:.2f}")

# task5
resNum = num1 // num2
print(f"Task5 birinchi sonni 2-songa butun bolinma :{resNum}")

# task6
numDiv = num1 % num2
print(f"Task6 1-sonni 2-songa bo`linma qoldiq :{numDiv}")

# Task7

aBPow = num1 ** num2
bAPow = num2 ** num1
farq = aBPow - bAPow
print(f"Task7: {num1} va {num2} sonlari uchun {num1}^{num2} va {num2}^{num1} sonlari orasidagi farq : {farq}")

# task8
r = int(input("Enter a radius: "))

area = 3.14 * r * r
print(f"Task8: Doira Yuzasi :{area}")

# Task9
sty = int(input("Xona uzunligi: "))
eni = int(input("Xona Eni:"))

pol = int(input("Xona Pol Qalinligi:"))

hajm = sty * eni * pol
print(f"Task9: Kub beton :{hajm}")

# Task10

p = 3.14
yol = int(input("Masofa:"))
shinaRadius = int(input("Shina Radius:"))

countShina = yol / 2 * p * r

print(f"Aylanishlar soni {countShina}")

# Task11

soniProduct = int(input("Mahsulotlar soni:"))  # 8000
ishchiSoni = int(input("Ishchilar count:"))  # 10
result = (soniProduct / ishchiSoni) / 8

print(f"1 soatda mahsulot : {result}")

# tomorrow  we learn list
