# 1. Duck typing
# 2. Operator overloading
# 3. Method overriding 
# 4. Method overloading

class duck:
    def swim(self):
        print("I am a duck , I can swim")
    def speaks(self):
        print("Quack Quack ")
        
class dog:
    def swim(self):
        print("I am a dog , I can swim") 
    def speaks(self):
        print("I can speak")

def display(obj):
     obj.swim()
     obj.speaks()
     print("Information delayed.......")

dog_1=dog()
duck_1=duck()
display(dog_1)
display(duck_1)