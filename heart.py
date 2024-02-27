import turtle

screen = turtle.getscreen()
t = turtle.Turtle()
t.speed(5000)
t.pensize(5)

for x in range(135):
    t.rt(1)
    t.fd(1)
for x in range (135):
    t.fd(1)
t.rt(90)
for x in range (135):
    t.fd(1)
for x in range(200):
    t.rt(1)
    t.fd(1)
t.lt(131)
for x in range (70):
    t.rt(1)
    t.fd(1)
# Keep the Turtle graphics window open

turtle.getscreen().mainloop()
