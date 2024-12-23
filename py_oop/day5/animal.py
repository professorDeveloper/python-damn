class Animal:
    def __init__(self, age, gender):
        self.age = age
        self.gender = gender

    def isMammal(self):
        return 'mammal'

    def mate(self, ):
        return 'mate'


class Duck(Animal):
    def __init__(self, beakColor, age, gender):
        super().__init__(age, gender)
        self.beakColor = beakColor

    def quack(self):
        return 'quack'

    def swim(self):
        return 'swim'


class Fish(Animal):
    def __init__(self, age, gender, sizeInFt: int, canEat):
        super().__init__(age, gender)
        self.__sizeInFt = sizeInFt
        self.__canEat = canEat

    def __swim(self):
        return 'swim'


class Zebra(Animal):
    def __init__(self, age, gender, isWild):
        super().__init__(age, gender)
        self.isWild = isWild

    def run(self):
        return 'run'


