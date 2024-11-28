number = int(input("4 xonali son kiriting:"))

birlar = number % 10
onlar = number // 10 % 10
yuzlar = number // 100 % 10
minglar = number // 1000 % 10
print(f"{minglar},{yuzlar},{onlar},{birlar}")



