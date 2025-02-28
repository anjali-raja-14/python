class Student:
    def __init__(self, name, rollnum, age):
        self.name = name  # Public attribute
        self._rollnum = rollnum  # Protected attribute (single underscore)
        self.__age = age  # Private attribute (double underscore)

    def display(self):
        print(f"Hi, my name is {self.name}, roll number is {self._rollnum}, and age is {self.__age}")

    def get_age(self):# getter method to acces the private member age 

        return self.__age
    
    def set(self,age): # setter method
        if(age>18):
            print("You can vote")
        else:
            self.__age=age

s1=Student("Ritesh",38,30)
print(s1.get_age())
s1.set(23)     



# provide security
# data security