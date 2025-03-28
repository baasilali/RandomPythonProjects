# Turtle Graphics and Loops
# Baasil Ali
# 09 / 27 / 2022

import turtle #Import turtle graphics
window = turtle.Screen() #Create a Screen for the turtle to draw on

t = turtle.Turtle() #reating the turtle object as t

for i in range(4): #For loop for square
    t.right(90) #Angle to turn
    t.forward(150) #Length of side

for i in range(2): #For loop for triangle roof
    t.left(120) #angle to turn
    t.fd(150) #Length of side


#raw_input() <- used this to keep window open after execution