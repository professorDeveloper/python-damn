class Dog:
    def __init__(self, age, breed):
        self.age = age
        self.breed = breed

    def bark(self):
        print(f"{self.breed} is barking")

    def eat(self):
        print(f"{self.breed} is eating")


dog = Dog(age=3, breed="Bulldog")
dog.bark()

dog2 = Dog(breed="Labrador", age=5)
dog2.eat()