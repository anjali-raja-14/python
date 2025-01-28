class A:
    def Class_A(self):
        print(" I am from class A")

class B(A):
    def Class_B(self):
        print("I am from class B & inherit class A")

class C(A):
    def Class_C(Self):
        print(" I am from class C & inherit class A ")

class D( B,C):
    def Class_D(self):
        print(" I am from class D & inherit class B & C ")


D_1=D()
D_1.Class_D()
print(D.mro())


