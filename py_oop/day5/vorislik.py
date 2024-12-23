class Car:
    def __init__(self, brand, fuel_capacity):
        self.brand = brand
        self.fuel_capacity = fuel_capacity

    def refuel(self, amount):
        if amount <= self.fuel_capacity:
            print(f"{self.brand} avtomobil {amount} litr yonilg'i bilan to'ldirildi.")
        else:
            print("Yonilg'i sig'imidan oshib ketdi.")

    def drive(self):
        print(f"{self.brand} haydash jarayonida.")


class ElectricCar:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity

    def charge(self, amount):
        if amount <= self.battery_capacity:
            print(f"Elektr avtomobil {amount} kVt batareya quvvati bilan zaryadlandi.")
        else:
            print("Batareya sig'imidan oshib ketdi.")

    def drive(self):
        print("Elektr avtomobil jim va samarali haydash jarayonida.")


class HybridCar(Car, ElectricCar):
    def __init__(self, brand, fuel_capacity, battery_capacity):
        Car.__init__(self, brand, fuel_capacity)
        ElectricCar.__init__(self, battery_capacity)

    def drive(self):
        print(f"{self.brand} gibrid avtomobili yonilg'i va elektr rejimida haydashda.")


toyota =Car(brand="Toyota",fuel_capacity=50)
toyota.refuel(40)
toyota.drive()

print(20*'-')

tesla = ElectricCar(battery_capacity=100)
tesla.charge(90)
tesla.drive()

print(20*'-')

# @HybridCar
hybrid_car = HybridCar(brand="Hybrid", fuel_capacity=50, battery_capacity=100)
hybrid_car.refuel(30)
hybrid_car.charge(60)
hybrid_car.drive()

