class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age


class Child(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self._school = school

    @property
    def school(self):
        return self._school

    def go_to_school(self):
        print(f"{self.name} is going to {self.school}")


person1 = Person("Azamov", 18)
print(person1.name)
print(person1.age)

child1 = Child("Azamov", 18, "Tashkent")
child1.go_to_school()
print(child1.name)
print(child1.age)
print(child1.school)
