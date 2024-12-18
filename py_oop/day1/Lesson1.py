class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def run(self):
        print(f"{self.name} is running")

    def sleep(self):
        print(f"{self.name} is sleeping")


saikou = Person("Saikou", 18, "Tashkent")
saikou.run()
print("=====================================================")
azamov = Person("Azamov", 18, "New York")
azamov.sleep()
