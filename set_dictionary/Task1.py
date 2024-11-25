#Task1
import math

num = int(input("Raqamni kiriting:"))
old_num =num
fact_num = 0
while num != 0:
    check_num = num % 10
    fact_num += math.factorial(check_num)
    num = num // 10

if fact_num==old_num:
    print(f"{old_num} Kuchli raqam")
else:
    print(f"{old_num} Kuchli raqam emas")


# 2-usuli with For
fact_num2 = 0
for i in str(old_num):
    fact_num2+=math.factorial(int(i))

if fact_num2==old_num:
    print(f"{old_num} Kuchli raqam")
else:
    print(f"{old_num} Kuchli raqam emas")
