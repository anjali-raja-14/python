class human:
    def __init__(self):
        self.nose=1
        self.ear=2
    def work(self):
        print("I can work")
    def eat(self):
        print("I can eat")
class male(human):
    def work(self):
        super().work()  # add the line i can eat (super class)
        print("This would override eat function")

male1=male()
male1.work()
print(male1.nose)
print(male1.ear)

