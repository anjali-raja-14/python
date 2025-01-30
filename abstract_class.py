# if action is same & implementation is diffrent we use abstract class

from abc import ABC,abstractmethod
class car(ABC):
    def show(self):
        print("Every car has 4 wheels")
    @abstractmethod  # decorator
    def speed(self): #  make the speed function abstract
        pass 

class maruti(car): # inherit car class
    def speed(Self):
        print("speed is 100 km/h")
class sezuki(car): # inherit car class
    def speed(self):
        print("speed is 70 km/h")

obj1=maruti()
obj1.show()
obj1.speed()

obj2=sezuki()
obj2.show()
obj2.speed()