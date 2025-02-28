"""
Same name but paas diffrent parameter
python doesn't support operator overloading with the use of default argument we can use the method_overloading 
with the use of *args we pass diffrent parameter

"""
class add:
    def add (self,*args):
       sum=0
       for i in args:
           sum=sum+i
       return sum
a=add()
print(a.add(1,5))
print(a.add(1,5,5))
print(a.add(1,5,8,3,3,3,5))
