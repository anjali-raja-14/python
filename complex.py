class Complex:
    def __init__(self,r,i):
        self.i=i
        self.r=r
    def __add__(self,c2):
        return complex(self.r+c2.r,self.i+c2.i)
    def __str__(self):
        return f"{self.i}+{self.r}i"

c1=Complex(1,2)
c2=Complex(3,4)
print(c1+c2)


   
