class Doctor:
    def __init__(self, name, age, gender, designation, salary):
        self.name = name
        self.age = age
        self.gender = gender
        self.designation = designation
        self.salary = salary

    def checkUp(self):
        print(f"{self.name}  checking up")

    def prescribe(self):
        print(f"{self.name}  prescribing")

    def eat(self):
        print(f"{self.name}  eating")

    def walk(self):
        print(f"{self.name}  walking")

docto1 =Doctor(name="Azamov",age=18,gender="male",designation="Dentist",salary=10000)
