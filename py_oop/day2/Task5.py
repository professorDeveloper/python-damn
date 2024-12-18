class Student:
    def __init__(self, name, age, gender,program, studyYear):
        self.name = name
        self.age = age
        self.gender = gender
        self.program = program
        self.studyYear = studyYear

    def study(self):
        print(f"{self.name}  studying")

    def eat(self):
        print(f"{self.name}  eating")

    def heldExam(self):
        print(f"{self.name}  held exam")

    def walk(self):
        print(f"{self.name}  walking")

student = Student("Azamov", 18, "male", "Python", 3)