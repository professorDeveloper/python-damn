class NewCard:
    def __init__(self, balance, card_number, date, pin_code):
        self.__balance = balance
        self.card_number = card_number
        self.date = date
        self.__pin_code = pin_code

    def set_pin_code(self, new_pin: str):
        if len(new_pin) == 4 and new_pin.isdigit():
            self.__pin_code = new_pin
            print("Pin kodi muvaffaqiyatli o`zgartirildi")
        else:
            print("Xato pin kodi")

    def set_balance(self, balance: int, pin_code: str):
        if pin_code == self.__pin_code:
            if balance > 0:
                self.__balance += balance
                print("Balance muvaffaqiyatli o`zgartirildi !")
            else:
                print("Xato qiymat balance")
        else:
            print("Pinkod xato")

    def get_pin_code(self):
        return self.__pin_code

    def get_balance(self):
        return self.__balance


card2 = NewCard(balance=10.0, card_number="8600130987654321", date="12/28", pin_code="4321")

card2.set_pin_code("1234")
print(f"Pin kodi: {card2.get_pin_code()}")
pin_code = input("Pin kodni kiriting")
card2.set_balance(1000, pin_code=pin_code)
