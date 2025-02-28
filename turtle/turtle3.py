from turtle import Turtle
a=Turtle()
a.shape("turtle")

def mini_circle():
    a.circle(40)
    a.lt(90)
    a.circle(40)
    a.lt(90)
    a.circle(40)
    a.lt(90)
    a.circle(40)
    a.lt(90)

def bigg_circle():
    a.circle(60)
    a.lt(90)
    a.circle(60)
    a.lt(90)
    a.circle(60)
    a.lt(90)
    a.circle(60)

a.begin_fill()
mini_circle()
bigg_circle()
a.end_fill()
a.speed("fast")











a.screen.mainloop()