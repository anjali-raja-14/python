
class girl: #base class
    def work(self):
        print("I can work")

class boy(girl): #inherit from girl class
    def eat(self):
        print("I can eat")

class human(boy):#inherit from boy classs
    pass
human_1=human()
human_1.eat()
human_1.work()


    