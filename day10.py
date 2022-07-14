def format_name(f_name,l_name):
  name=f_name.title()
  l_n=l_name.title()
  print(name+" "+l_n)
format_name("shru","tayy")

#Functions with Outputs
def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  f"Result: {formated_f_name} {formated_l_name}"

#Storing output in a variable
formatted_name = format_name(input("Your first name: "), input("Your last name: "))
print(formatted_name)
#or printing output directly
print(format_name(input("What is your first name? "), input("What is your last name? ")))

#Already used functions with outputs.
length = len(formatted_name)

#Return as an early exit
def format_name(f_name, l_name):
  """Take a first and last name and format it 
  to return the title case version of the name."""
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"Result: {formated_f_name} {formated_l_name}"




from art import logo
print("welcome to this cheap random calculator")
print(logo)
a=input("enter number")
b=input("other number")
print("enter + for add, - for minus ,* for multiply ,/ for divide ,** fo power")
c=input("symbol")
""" 
this 
is 
multiline
comm"""
def calc(c):
  s=0
  if c=="+":
    s=int(a)+int(b)
    print(s)
  elif c=="-":
    s=int(a)-int(b)
    print(s)
  elif c=="*":
    s=int(a)*int(b)
    print(s)
  elif c=="/":
    s=int(a)/int(b)
    print(s)

calc(c)
    
    
  



def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year,month):
 # month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  p=is_leap(year)
  if p==True:
    print(28)
  if p==False and month%2==0:
      print(30)
  if p==False and month%2!=0:
      print(31)

  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


from replit import clear
from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()










