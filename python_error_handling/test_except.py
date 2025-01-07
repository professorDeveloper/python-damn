class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

def getDriveLicense(age:int):
    """
    Haydovchilik guvohnoma uchun yoshni tekshiradi.
    Agar Yosh 18 dan kichik bo`lsa CustomError qaytaradi.
    """
    if not isinstance(age, int):
        raise CustomError("Yosh butun son` bo'lishi kerak")
    if age < 18:
        raise CustomError("Haydashga ruxsat berilmagan")
    else:
        print("Ruxsat berildi")



def transferMoney(cardNumber:int, amount:int):
    """
    Pul o`tkazish uchun karta raqamini va summani tekshiradi.
    Agar summa yoki karta raqam manfiy bo`lsa Custom qaytaradi
    """
    if not isinstance(cardNumber, int):
        raise CustomError("Karta raqam butun son bo'lishi kerak")
    if not isinstance(amount, int):
        raise CustomError("Summa butun son bo'lishi kerak")
    if amount < 0:
        raise CustomError("Summa manfiy bo'lishi mumkin emas")
    else:
        print("Muvaffaqiyatli chiqarildi")


try:
    getDriveLicense(17)
    transferMoney(1234, 1000)
except CustomError as e:
    print(e.message)
except Exception as e:
    print(e)
