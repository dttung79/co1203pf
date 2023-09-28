import turtle
j = turtle.Turtle()
j.speed(50)
j.pensize(4)
j.circle(130)
j.right(90)
j.forward(160)
j.left(90)
j.penup()
j.goto(-100,170)
j.pendown()
j.fillcolor("yellow")
j.begin_fill()
for i in range(5):
    j.forward(200)
    j.right(144)
j.end_fill()

turtle.done()