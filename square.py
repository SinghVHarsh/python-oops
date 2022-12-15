from polygon import Polygon
from shape import Shape
class Square(Polygon,Shape):#this is a child or derived class
    def area(self):
        return self.get_height( ) * self.get_width()
