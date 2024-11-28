# Reverse Integer

num = int(input("Raqam kiriting: "))
isManfiy = num < 0
numStr = str(abs(num)) # moduledan chiqarish
numList = list(numStr) # listga ogirish va reverese qilish
numList.reverse() # Reverse qilish
numStr = "".join(numList) #stringa o`girish

natija = int(numStr) # string to inte
if isManfiy: # manfiyga tekshirish
    natija = -natija
    #

print(natija)
