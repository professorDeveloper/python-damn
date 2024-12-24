class  Shape:
    def __init__(self,area):
        self._area = area

    def getArea(self):
        return self._area


class Rectangle(Shape):
    def __init__(self,length,width,area):
        super().__init__(area)
        self._length = length
        self._width = width

    def getArea(self):
        return super().getArea()


class Circle(Shape):
    def __init__(self,radius,area):
        super().__init__(area)
        self._radius = radius

    def getArea(self):
        return super().getArea
