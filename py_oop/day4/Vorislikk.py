class Person:
    def __init__(self, age: int, name: str):
        self.__age = age
        self.name = name
    def set_age(self, age):
        if age>0:
            self.__age = age
    def get_age(self):
        return self.__age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

person1 = Person(18, "Azamov")

print(person1.name)