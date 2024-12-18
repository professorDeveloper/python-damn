class Student:
    name: str
    age: str
    color: str

    def eating(self):
        print(f"{self.name} is eating")

    def drinking(self):
        print(f"{self.name} is drinking")

    def running(self):
        print(f"{self.name} is running")


class Student2:
    name: str
    age: str
    color: str

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def sleeping(self):
        print(f"{self.name} is sleeping")


student1 = Student()

student1.name = "Azamov"
student1.age = 18
student1.color = None
print(student1.name)
student1.running()

student2 = Student2(name="Saikou", age=124, color="COLO")
print(student2.name)
student2.sleeping()
