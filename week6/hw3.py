# Write a program that draws n squares of multiple random colors.
# All squares are of the same size and moving around a corner (top left corner).
# The program will ask for n, then draw n squares.
import turtle as t
import random as rd
t.speed(0)

size = 100
angle = 90
t.colormode(255)

n = int(input('Enter n: '))
for i in range(n):
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)
    t.pencolor(r, g, b)

    for j in range(4):
        t.forward(size)
        t.left(angle)
    
    t.left(360 / n)

t.exitonclick()
