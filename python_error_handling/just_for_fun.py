# print(10 / 0)  # ZeroDivisionError
#
# print("10" + 10)  # TypeError
#
# list = [1, 2, 3]
# print(list[3])  # IndexError
#
# d = {"a": 1, "b": 2}
# print(d["c"])  # KeyError
#
# print(int("abc")) #ValueError
#
from curses.ascii import isdigit


class FormatError(Exception):
    def __init__(self,message):
        self.message=message
        super.__init__(message)


def check_format(phone_number:str)->bool:
    """
    Telefon raqami to`g`ri formatda ekanligini
    tekshirish uchun
    agar telefon raqam string toifasida bo`lmasa FormatError qaytaradi
    """
    if not isinstance(phone_number,str):
        raise FormatError("Telefon raqami string toifasida bo`lmadi")
    elif len(phone_number) == 13 and phone_number[1:].isdigit():
        return True
    else:
        return False

try:
    check_format(phone_number=998916543215)
except FormatError as e:
    print(e)
except Exception as e:
    print(e)