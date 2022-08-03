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
