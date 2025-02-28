
from turtle import Turtle, Screen

def main():
    screen = Screen()
    tom = Turtle()
    screen.listen()

    def up():
        tom.setheading(90)
        tom.forward(20)

    def down():
        tom.setheading(270)
        tom.forward(20)

    def left():
        tom.setheading(180)
        tom.forward(20)

    def right():
        tom.setheading(0)
        tom.forward(20)

    screen.onkey(fun=up, key="Up")
    screen.onkey(fun=down, key="Down")
    screen.onkey(fun=left, key="Left")
    screen.onkey(fun=right, key="Right")

    screen.exitonclick()

if __name__ == "__main__":
    main()


