## Tuple bu pythondagi imutable list hisoblanadi yani yaratilgan itemlar ozgarmas bo`ladi

# Tuple yaratish  -> Typle yaratish uchun elementlar qavz ichida yoziladi elementlar vergul bilan ajiratiladi.
# Tuple`ning asosiy xususiyati - uni yaratganingizdan keyin uni o`zgartirib bo`lmaydi


tuples = (4, 3,)
print(type(tuples))  # <class 'tuple'>

# Tuple dagi elementlarga index orqali murojat qilish
my_tuple = ("a", "b", "c")
print(my_tuple[1])

# Tuple da malumot o`zgartirish mumkin emas

my_tuple = ("a", "b", "c")
# my_tuple[1] = '3'  # Bu type Error ga olib keladi

# Tuple ning asosiy foydali jihati bu listdagi malumotlarni enkapsulatsiya yani set methodlaridan cheklash !

# Tuple ni listga o`zgartirish
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)

# List ni tuple ga o`zgartirish
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)
# natija
# [1,2,3]
# (1,2,3)
