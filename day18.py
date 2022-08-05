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
