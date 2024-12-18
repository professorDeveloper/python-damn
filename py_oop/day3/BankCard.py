import keyword


class BankCard:
    def __init__(self, balance: float, card_number: str, date: str, pin_code: str):
        self.balance = balance
        self.card_number = card_number
        self.date = date
        self.pin_code = pin_code

    def info(self):
        print("Say hello")


card1 = BankCard(0.0, card_number="8600130987654321", date="12/28", pin_code="1234")

card1.balance = 1000
card1.card_number = "8600130987654321"
card1.pin_code = "4321"


