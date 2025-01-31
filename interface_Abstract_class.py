# all child method couls be abstract class
from abc import ABC,abstractmethod

class shape(ABC): # inherit ABC class
    @abstractmethod
    def show(self):
        pass
    @abstractmethod
    def color(self):
        pass

class circle(shape):
    
    def show(self):
        print("circle has no sides..........")
    def color(self):
        print("Blue")

class square(shape):
    def show(self):
        print("square has 4 sides..........")
    def color(self):
        print("Red")
circle_1=circle()
circle_1.show()
circle_1.color()

square_1=square()
square_1.show()
square_1.color()