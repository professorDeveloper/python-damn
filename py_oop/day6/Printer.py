
class Printer:
    def __init__(self, quality):
        self.__quality = quality

    def setQuality(self, quality):
        self.__quality = quality

    def print(self, text):
        print(text)


class LazerPrinter(Printer):
    def print(self, text):
        print(text.upper())


class InkjetPrinter(Printer):
    def print(self, text):
        print(text.lower())


class FaxMachine(Printer):
    def print(self, text):
        print(text + " .")


lazerPrinter = LazerPrinter(100)
inkjetPrinter = InkjetPrinter(100)
faxMachine = FaxMachine(100)

lazerPrinter.print("Salom")
inkjetPrinter.print("Hi")
faxMachine.print("Hello")
