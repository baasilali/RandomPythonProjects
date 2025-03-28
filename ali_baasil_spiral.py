# Turtle Graphics and Loops
# Baasil Ali
# 09 / 28 / 2022

import turtle
window = turtle.Screen()

t = turtle.Turtle()

sides = input("Enter the # of sides you would like to draw: ")
iterations = input("Enter the # of iterations: ")
percentIncrease = input("Enter the percent increase to be made for each arm: ")

size = 10
angle = float(((float(sides) - 2) * 180.0) / float(sides))
angle = 180 - angle

t.pensize(2)

for i in range(int(iterations)):
    t.forward(size)
    t.right(angle)
    size = size + (float(percentIncrease) / 100) * size


turtle.done()



