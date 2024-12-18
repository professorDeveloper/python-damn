class Animals:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating")


cat = Animals(name="Kitty", age=2)
cow = Animals(name="Cow", age=5)
cat.eat()

