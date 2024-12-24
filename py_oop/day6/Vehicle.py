class Vehicle:

    def goBackward(self, speed: float, accel: float):
        print(f" {speed} and Accel {accel}")

    def goForward(self, speed: float, accel: float):
        print(f" {speed} and Accel {accel}")

    def start(self):
        return True

    def stop(self):
        print("Nothing")


class Dumptruck(Vehicle):
    def __init__(self, loadCapacity, numsWheel, weight):
        self.__loadCapacity = loadCapacity
        self.__numsWheel = numsWheel
        self.__weight = weight

    def lowerLoad(self):
        return None

    def raiseLoad(self):
        return None


class Pickup(Vehicle):
    def __init__(self, loadCapacity, numsWheel, weight):
        self.__loadCapacity = loadCapacity
        self.__numsWheel = numsWheel
        self.__weight = weight


class Car(Vehicle):
    def __init__(self, numsWheel, weight):
        self.__numsWheel = numsWheel
        self.__weight = weight


class Convertible(Car):
    def __init__(self, numsWheel, weight):
        super().__init__(numsWheel, weight)

    def lowerRoof(self):
        return True
