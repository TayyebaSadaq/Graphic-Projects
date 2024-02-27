import turtle
t = turtle.Turtle()
s = turtle.Screen()

for x in range (35):
    t.forward(x)
    t.left(x)
    t.right(10)
t.left(180)
for x in range (35):
    t.forward(x)
    t.right(x)
    t.left(10)
# Keep the Turtle graphics window open
turtle.getscreen().mainloop()
