class Human:
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")

class Male(Human):  #inherit human class
    pass
   
male1=Male()
male1.eat()

class Female(Male):
    pass
female1=Female()
female1.work()