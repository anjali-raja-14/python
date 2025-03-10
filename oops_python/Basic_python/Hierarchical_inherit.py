class human:
    def work(self):
        print("I can work")
    def play(self):
        print("I can play")

class girl(human):
    pass
class boy(human):
    pass

girl_1=girl()
girl_1.work()
boy_1=boy()
boy_1.play()