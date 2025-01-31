class Student:
    def __init__(self,name,rollnum,age):
        self.name=name # public name
        self._rollnum=rollnum # protected used underscore _
        self.__age=age #private used undeescore undeescore _ _
        #not able to access
        
    def display(self):
        print(f"Hi, my name is {self.name}, roll number is {self._rollnum}  & age is {self.__age}")

    def display_private_data(self):
        self.display()

student=Student("Anjali","DS6A2305",20)
student.display_private_data() # access private members

# class Branch(Student):
#     pass 
# def Show_data():
#     b1=Branch("Yash","33")
#     print(b1.name,b1._rollnum)
   
# Show_data()
# b1=Branch("Rahul","45")
# b1.name="Ritesh" #update data
# b1._rollnum=87
# b1.display()
