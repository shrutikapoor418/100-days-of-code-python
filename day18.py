#draw box using turtle graphics

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from turtle import *
tim_tu = Turtle()
tim_tu.shape("circle")
tim_tu.color("green")
tim_tu.forward(100)
tim_tu.left(90)
tim_tu.backward(100)
tim_tu.right(90)
tim_tu.backward(100)
screen = Screen()
tim_tu.left(90)
tim_tu.forward(100)
screen.exitonclick()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import turtle as t

tim = t.Turtle()

########### Challenge 2 - Draw a Dashed Line ########
for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
import turtle as t

tim = t.Turtle()

########### Challenge 2 - Draw a Dashed Line ########
no_of_sides=5
for _ in range(no_of_sides):
    angle=360/no_of_sides
    tim.forward(100)
    tim.right(angle)
no_of_sides=4
for _ in range(no_of_sides):
   madangle=360/no_of_sides
   tim.forward(100)
   tim.right(madangle)

no_of_sides=3
for _ in range(no_of_sides):
   madangles=360/no_of_sides
   tim.forward(100)
   tim.right(madangles)


#turtle with colors
import turtle as t
import random

tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 20):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)
