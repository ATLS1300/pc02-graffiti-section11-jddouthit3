#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: John Douthit
September 2, 2021
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
leftEye = (-15, 108)
leftForehead = (-15, 150)
rightForehead = (33, 155)
nose = (24, 84)
chin = (25, 10)
rightShoulder = (146, -63)
fingertipClose = (120, -90)
littleHome = (330,-125)
littleHome2 = (328, -120)

#begin drawing
turtle.up()
turtle.goto(leftEye)
turtle.color("DarkRed")
turtle.down()
turtle.begin_fill()
turtle.circle(7)
turtle.end_fill()
#nexteye
turtle.up()
turtle.goto(43,116)
turtle.down()
turtle.begin_fill()
turtle.circle(7)
turtle.end_fill()
#finger lazers
turtle.up()
turtle.pensize(7)
turtle.color("Red")
turtle.goto(fingertipClose)
turtle.right(10)
turtle.down()
turtle.forward(50)

turtle.up()
turtle.forward(20)
turtle.down()
turtle.forward(50)

turtle.up()
turtle.forward(20)
turtle.down()
turtle.forward(50)

#littleperson
 #rightleg
turtle.color("HotPink")
turtle.pensize(3)
turtle.up()
turtle.goto(littleHome)
turtle.right(60)
turtle.down()
turtle.forward(25)
#leftleg
turtle.up()
turtle.goto(littleHome)
turtle.right(30)
turtle.down()
turtle.forward(25)
#body
turtle.up()
turtle.goto(littleHome)
turtle.right(160)
turtle.down()
turtle.forward(30)
#head
turtle.up()
turtle.begin_fill()
turtle.down()
turtle.circle(7)
turtle.end_fill()
#rightarm
turtle.up()
turtle.goto(littleHome2)
turtle.right(25)
turtle.down()
turtle.forward(25)

turtle.up()
turtle.goto(littleHome2)
turtle.right(15)
turtle.down()
turtle.forward(25)

#thirdeye
turtle.color("Black")
turtle.up()
turtle.goto(leftForehead)
turtle.left(5)
turtle.down()
turtle.forward(35)

turtle.up()
turtle.right(120)
turtle.down()
turtle.forward(35)

turtle.up()
turtle.right(120)
turtle.down()
turtle.forward(35)
#circle
turtle.color("LimeGreen")
turtle.pensize(4)
turtle.up()
turtle.begin_fill()
turtle.goto(3,170)
turtle.down()
turtle.circle(7)
turtle.end_fill()

turtle.up()
turtle.goto(3,165)
turtle.down()
turtle.color(255,255,0)
turtle.begin_fill()
turtle.circle(2)
turtle.end_fill()
#polygon
turtle.up()
turtle.pensize(5)
turtle.color(109,120,113)
turtle.goto(365,-150)
turtle.down()
turtle.begin_fill()
turtle.goto(365,-250)

turtle.goto(-370,-250)

turtle.goto(-370,-150)

turtle.goto(365,-150)
turtle.end_fill()

#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#turtle.done()
