class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def walk(self):
        print(f"{self.name} is walking")

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def work(self):
        print(f"{self.name} is working")


azamov = Person("Azamov", 18, "New York")
azamov.walk()
azamov.eat()
azamov.sleep()
azamov.work()
