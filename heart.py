import turtle

screen = turtle.getscreen()
t = turtle.Turtle()
t.pensize(5)
t.speed("fastest")

# Draw Heart
def heart(color):
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()

    for x in range(135):
        t.rt(1)
        t.fd(1)
    for x in range(135):
        t.fd(1)
    t.rt(90)
    for x in range(135):
        t.fd(1)
    for x in range(200):
        t.rt(1)
        t.fd(1)
    t.lt(131)
    for x in range(70):
        t.rt(1)
        t.fd(1)

    t.end_fill()

heart("red") 
t.up()
t.goto(100, 200)
t.down()
heart("blue")

# Keep the Turtle graphics window open
turtle.getscreen().mainloop()
