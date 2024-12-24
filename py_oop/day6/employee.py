class Employee:
    def __init__(self, name, started):
        self.name = name
        self.started = started

    def setName(self, name):
        self.name = name

    def setStarted(self, started):
        self.started = started


class FullTimeEmployee(Employee):
    def __init__(self, name, started, positioner):
        super().__init__(name, started)
        self.positioner = positioner

    def setPositioner(self, positioner):
        self.positioner = positioner


class PartTimeEmployee(Employee):
    def __init__(self, name, started, hours):
        super().__init__(name, started)
        self.hours = hours

    def setHours(self, hours):
        self.hours = hours

