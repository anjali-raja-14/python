# print(int.__add__(1,2))
# print(str.__add__("1","2"))



# class Complex_num:
#     def __init__(self,r,i):
#         self.real=r
#         self.imaginary=i
#     def __add__(self,other):
#         return f"{self.real+other.real}+{self.imaginary+other.imaginary}i"
# c1= Complex_num("1","2")
# c2= Complex_num("4","5")# str concatenate
# # o/t= 14+25i

# c3= Complex_num(1,2)
# c4= Complex_num(4,5)
# # o/t= 5+7i

# print(c1+c2)
# print(c3+c4)



class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __gt__(self,other):
        pass
        if(self.age>other.age):
            return True
        else:
            return False

P1=Person("Anjali",20)
P2=Person("Ritesh",30)

if(P1>P2):
    print( f"{P1.name} will pay the bill")

if(P1<P2):
    print (f"{P2.name} will pay the bill")


        



