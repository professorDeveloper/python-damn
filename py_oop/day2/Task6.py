class Teacher:
    def __init__(self, name, age, gender, designation, salary):
        self.name = name
        self.age = age
        self.gender = gender
        self.designation = designation
        self.salary = salary

    def teach(self):
        print(f"{self.name} is teaching")

    def takeExam(self):
        print(f"{self.name} is taking exam")

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


teacher = Teacher(name="Azamov",age=18,gender="male",designation="Teacher",salary=10000)
teacher2 = Teacher(name="Sultanbek",age=18,gender="male",designation="Teacher",salary=10000)

