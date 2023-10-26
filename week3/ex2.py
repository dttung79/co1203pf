# Ask user to choose which shape to draw (square or triangle)
# If user choose square then draw a square
# Else if user choose triangle then draw a triangle
# If not square or triangle, tell user that you cannot draw that
import turtle as t

shape = input('Which shape do you want to draw (square / triangle)? ')
length = 100

if shape == 'square':
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.exitonclick()
elif shape == 'triangle':
    t.forward(length)
    t.left(120)
    t.forward(length)
    t.left(120)
    t.forward(length)
    t.left(120)
    t.exitonclick()
else:
    print('Cannot draw that shape!')