class Father:
    def eat(self):
        print(" I can eat at 5:00 PM")
    def sleep(self):
        print(" I will sleep at 10:00 PM ")
class Son(Father):
    def eat(self):
        print(" I can eat at 6:00 PM")
        super().eat()
Ram=Son()
Ram.eat() # This will print  I can eat at 6 pm
#Override the eat function of father
 

