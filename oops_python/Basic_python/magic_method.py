class Author:
    def __init__(self,Name,Roll_num):
        self.Name=Name
        self.Roll_num=Roll_num
   
    def __str__(self):
        return f" {self.Name} , {self.Roll_num}"
    def __len__(self):
        return self.Roll_num # magic method
    def __call__(self, *args, **kwds):
        print("hii")
    def __del__(self):
        print("Class has been deleted...........")

a=Author("Anjali",235678)
print(a)
print(len(a)) 
a() 
# it is not callable bcs of ..magic method it is callable
del(a) # del the class a

   