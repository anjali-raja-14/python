class Human: #base class
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")

#inherit human class
class Male(Human):  # derived class from human class
    pass
   
male1=Male()
male1.eat()

class Female(Male): # derived class from Male class
    pass
female1=Female()
female1.work()

