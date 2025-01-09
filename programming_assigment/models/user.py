from programming_assigment.models.car_number import CarNumber
from programming_assigment.models.message import Message


class User:
    __chatList : list[Message] =[]
    __myCarNumbers: list[CarNumber] = []

    def __init__(self, name, email, password, id):
        self.id = id
        self.email = email
        self.password = password
        self.name = name

    @@property
    def getChatList(self):
        return self.__chatList

    @property
    def getMyCarNumbers(self):
        return self.__myCarNumbers

    @getMyCarNumbers.setter
    def updateMyCarNumbers(self, myCarNumbers):
        self.__myCarNumbers = myCarNumbers