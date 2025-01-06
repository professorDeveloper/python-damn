class Card:
    cardNumber :int
    cardDate:str
    pinCode:int
    __balance:int

    def __init__(self, cardNumber, cardDate,pinCode):
        self.__balance = 0
        self.cardDate=cardDate
        self.pinCode=pinCode
        self.cardNumber=cardNumber

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):

        pinCode = int(input("Balans qo`shish uchun Pin kodni kiriting:"))
        if pinCode==self.pinCode:
            if balance>0:
                self.__balance+=balance
                print("Balance muvaffaqiyatli o`zgartirildi !")
            else:
                print("Xato qiymat balance")
        else:
            print("Pinkod xato")

card1 =Card(8600130987654321,"12/28",4321)

print("Joriy Balans:",card1.balance)

card1.balance=100

