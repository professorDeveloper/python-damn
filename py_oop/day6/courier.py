class Courier:
    def __init__(self, name, home_country):
        self.name = name
        self.home_country = home_country

    def calculateShipping(self):
        return 0.0

    def ship(self):
        return False


class MonotypeDelivery(Courier):
    def __init__(self, name, home_country):
        super().__init__(name, home_country)

    def ship(self):
        return True


class PigeonHost(Courier):
    def __init__(self, name, home_country):
        super().__init__(name, home_country)

    def ship(self):
        return False


courier = PigeonHost("", "Name")
courier.calculateShipping()
