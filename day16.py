from turtle import Turtle,Screen
tim=Turtle()
print(tim)
tim.shape("turtle")
tim.color("coral")
tim.forward(100)
print()
another_var=10
my_screen=Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
another_module.py
from turtle import Turtle
tim=Turtle()
print(tim)
another_var=10

#tables in python
from prettytable import PrettyTable

# Specify the Column Names while initializing the Table
myTable = PrettyTable(["Student Name", "Class", "Section", "Percentage"])

# Add rows
myTable.add_row(["ram", "1", "B", "91.2 %"])
myTable.add_row(["luxman", "2", "C", "63.5 %"])
myTable.add_row(["bharat", "3", "A", "90.23 %"])
myTable.add_row(["shatrugan", "4", "D", "92.7 %"])
myTable.add_row(["hanuman", "X", "5", "98.2 %"])
myTable.add_row(["madhav", "X", "1", "88.1 %"])
myTable.add_row(["pavan putra", "1", "B", "95.0 %"])

print(myTable)

from prettytable import PrettyTable

columns = ["Student Name", "Class", "Section", "Percentage"]

myTabl = PrettyTable()

# Add Columns
myTabl.add_column(columns[0], ["Leanord", "Penny", "Howard",
					"Bernadette", "Sheldon", "Raj", "Amy"])
myTabl.add_column(columns[1], ["X", "X", "X", "X", "X", "X", "X"])
myTabl.add_column(columns[2], ["B", "C", "A", "D", "A", "B", "B"])
myTabl.add_column(columns[3], ["91.2 %", "63.5 %", "90.23 %", "92.7 %",
										"98.2 %", "88.1 %", "95.0 %"])

print(myTabl)


