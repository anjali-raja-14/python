# # import math
# # a=int(input("Enter the length: "))
# # b=int(input("Enter the breadth: "))
# # c=a*b
# # no_of_cans=(a*b)/7
# # print((a*b)/7)
# # # 1 can paint 7 m area 
# # print(math.ceil(no_of_cans))



# import turtle
# i=True
# turtle.speed("fastest")
# while i!=150:
#     turtle.fd(i)
#     turtle.circle(i)
#     turtle.lt(90)
#     turtle.circle(i)
#     turtle.fd(i)
#     turtle.circle(i)
#     turtle.lt(90)
#     turtle.circle(i)
#     turtle.fd(i)
#     turtle.circle(i)
#     turtle.lt(90)
#     turtle.circle(i)
#     turtle.fd(i)
#     turtle.circle(i)
#     i+=1
# turtle.mainloop()



from turtle import Turtle,Screen
def square(a):
    a.penup()
    a.goto(200,100)
    a.shape("square")
    a.color("red","green")
    a.pensize(5)
    a.pendown()
    a.setheading(0)
    for i in range(4):
        a.fd(100)
        a.lt(90)
def circle(a):
    a.pu()
    a.setposition(-200,100)
    a.shape("circle")
    a.color("yellow","green")
    a.pensize(5)
    a.pd()
    a.setheading(0)
    a.circle(50)
def triangle(a):
    a.up()
    a.setpos(-200,-100)
    a.shape("triangle")
    a.color("green","green")
    a.pensize(5)
    a.down()
    a.setheading(-120)
    # a.rt(120)
    for i in range(3):
        a.fd(100)
        a.lt(120)
def pentagon(a):
    a.up()
    a.goto(169.10,-100)
    a.shape("classic")
    a.color("cyan","green")
    a.pensize(5)
    a.down()
    a.setheading(0)
    a.rt(72)
    for i in range(5):
        a.fd(100)
        a.lt(72)
def main():
    a=Turtle()
    a.speed("slow")
    square(a)
    circle(a)
    triangle(a)
    pentagon(a)
    a.screen.mainloop()
main()