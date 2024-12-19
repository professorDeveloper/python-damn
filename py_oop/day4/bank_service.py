# Bank Service

class Bank:
    def __init__(self, balance, card_number, date, pin_code):
        self.__balance = balance
        self.card_number = card_number
        self.date = date
        self.__pin_code = pin_code

    @property
    def pin_code(self):
        return self.__pin_code

    @pin_code.setter
    def pin_code(self, new_pin):
        if len(new_pin) == 4 and new_pin.isdigit():
            self.__pin_code = new_pin
            print("Pin kodi muvaffaqiyatli ozgartirildi")
        else:
            print("Xato pin kodi")

    @property
    def balance(self):
        pin_code = input("Pin kodni kiriting:")
        if pin_code == self.__pin_code:
            return f"Balans:{self.__balance}"
        else:
            return "Pin kod xato !"

    @balance.setter
    def balance(self, newBalance:int):
        if newBalance > 0:
            self.__balance = newBalance
            print("Balance muvaffaqiyatli ozgartirildi !")
        else:
            print("Xato qiymat balance")

    def withdraw_balance(self, amount:int, pincode):
        if pincode == self.__pin_code:
            if 0 < amount <= self.__balance:
                self.__balance -= amount
                print("Balance muvaffaqiyatli chiqarildi !")
            else:
                print("Mablag` yetarli emas yoki qiymat xato")
        else:
            print("Pin kod xato")


bank = Bank(balance=0, card_number="8600130987654321", date="12/28", pin_code="1234")


while True:
    print("1. Mening Balansim")
    print("2. Balansni O'zgartirish")
    print("3. Parolni almashtirish")
    print("4. Balansdan Yechish")
    print("5. Bank malumoti")
    print("6. Chiqish")
    choice = input("Tanlovni kiriting: ")

    if choice == "1":
        print(bank.balance)
    elif choice == "2":
        newBalance = int(input("Yangi balansni kiriting: "))
        bank.balance = newBalance
    elif choice == "3":
        new_pin = input(f"Yangi pin kodni kiriting :")
        if len(new_pin) == 4 and new_pin.isdigit():
            current_pin = input("Joriy pin kodni kiriting: ")
            if current_pin == bank.pin_code:
                bank.pin_code = new_pin
                print("Pin kod muvaffaqiyatli o'zgartirildi!")
            else:
                print("Joriy pin kod xato!")
        else:
            print("Xato pin kodi! Pin kod faqat 4 ta raqamdan iborat bo'lishi kerak.")
    elif choice == "4":
        amount = int(input("Yechish summasini kiriting: "))
        pincode = input("Pin kodni kiriting:")
        bank.withdraw_balance(amount, pincode)
    elif choice == "5":
        pin_code = input("Pin kodni kiriting:")
        if pin_code == bank.pin_code:
            print("Bank malumoti:")
            print(f"Card Number: {bank.card_number}")
            print(f"Date: {bank.date}")
        else:
            print("Pin kod xato!")
    elif choice == "6":
        print("Dastur tugadi !")
        break
