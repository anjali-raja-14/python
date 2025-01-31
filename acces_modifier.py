class Student:
    def __init__(self, name, rollnum, age):
        self.name = name  # Public attribute
        self._rollnum = rollnum  # Protected attribute (single underscore)
        self.__age = age  # Private attribute (double underscore)

    def display(self):
        print(f"Hi, my name is {self.name}, roll number is {self._rollnum}, and age is {self.__age}")

    def display_private_data(self):
        self.display()

# Creating an object of Student
student = Student("Anjali", "DS6A2305", 20)

# Accessing public and protected members
print(student.name)        # Accessible
print(student._rollnum)    # Accessible (not recommended, as it's intended to be protected)

# Accessing private members using name mangling
print(student._Student__age)  # Works, but not recommended

# Calling a method to access private data
# student.display_private_data()


# Inheriting Student class in Branch
class Branch(Student):
    def __init__(self, name, rollnum, age):
        super().__init__(name, rollnum, age)  # Call parent constructor

# Function to demonstrate access to attributes in subclass
def Show_data():
    b1 = Branch("Yash", "33", 21)
    print(b1.name, b1._rollnum)
   
Show_data()

# Updating attributes
b1 = Branch("Rahul", "45", 22)
b1.name = "Ritesh"  # Updating public attribute
b1._rollnum = 87    # Updating protected attribute (not recommended)

b1.display()
