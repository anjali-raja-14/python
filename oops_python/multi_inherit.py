class girl:
    def work(self):
        print("I can work")
    def eat(self):
        print("I can eat")

class boy:
    def drink(self):
        print("I can drink")
    def flirt(self):
        print("I can flirt")

class human(girl,boy): #inherit girl & boy class
    pass

human_1=human()
human_1.work()
human_1.eat()
human_1.flirt()
human_1.drink()

