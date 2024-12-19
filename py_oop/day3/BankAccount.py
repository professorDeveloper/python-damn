class BankAccount:
    def __init__(self, balance: int, card_number, date, pin_code):
        self.__balance = balance
        self.card_number = card_number
        self.date = date
        self.__pin_code = pin_code

    def set_balance(self, pin_code, balance):
        if pin_code == self.__pin_code:
            if balance > 0:
                self.__balance += balance
                print("Balance muvaffaqiyatli Qo`shildi !")
            else:
                print("Xato qiymat balance")
        else:
            print("Pin kod xato")

    def get_balance(self):
        return self.__balance

    def withdraw_balance(self, amount, pincode):
        if pincode == self.__pin_code:
            if 0 < amount <= self.__balance:
                self.__balance -= amount
                print("Balance muvaffaqiyatli chiqarildi !")
            else:
                print("Xato qiymat balance")
        else:
            print("Pin kod xato")

    def get_pin_code(self):
        return self.__pin_code


account1 = BankAccount(0, "8600130987654321", "12/28", "1234")
account1.get_balance()
pin_code = input("Pin kodni kiriting")
account1.set_balance(balance=100, pin_code=pin_code)
