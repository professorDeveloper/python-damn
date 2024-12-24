class SuperClass1:

    def __init__(self, atribut1):
        self.atribut1 = atribut1

    def setAtribut1(self, atribut1):
        self.atribut1 = atribut1


class SuperClass2:

    def __init__(self, atribut2):
        self.atribut2 = atribut2

    def setAtribut2(self, atribut2):
        self.atribut2 = atribut2


class SubClass(SuperClass1, SuperClass2):

    def __init__(self, atribut1, atribut2):
        super().__init__(atribut1)
        super().__init__(atribut2)

    def setAtribut1(self, atribut1):
        print("Atribut1 working")

    def setAtribut2(self, atribut2):
        print("Atribut2 working")


object1 = SubClass(1, 2)
object1.setAtribut1(3)
object1.setAtribut2(4)
