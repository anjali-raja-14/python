class Circle:
    pi=3.1
    def __init__(self,radius):
        self.radius=radius
        self.area=Circle.pi*radius*radius
        self.circum=Circle.pi*radius*radius

    def get_circumference(self): #method
        return 2*Circle.pi*self.radius
    
circle_1=Circle(3)

print(circle_1.get_circumference())
print(circle_1.area)
print(circle_1.circum)

    
              