# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
def greeot():
  print("ok")
  print("ol")
  print("lo")

greeot()

 #Simple Function
def greet():
  print("Hello shru")
  print("How do you do shru?")
  print("Isn't the weather nice today?")
greet()

#Function that allows for input
#'name' is the parameter.
#'Jack Bauer' is the argument.
def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How do you do {name}?")
greet_with_name("bhavya")

#Functions with more than 1 input
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}?")

#Calling greet_with() with Positional Arguments
greet_with("shrutu", "Nowhere")

#Calling greet_with() with Keyword Arguments
greet_with(location="shh", name="A")

 #Simple Function
def greet():
  print("Hello shru")
  print("How do you do shru?")
  print("Isn't the weather nice today?")
greet()

#Function that allows for input
#'name' is the parameter.
#'Jack Bauer' is the argument.
def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How do you do {name}?")
greet_with_name("bhavya")

#Functions with more than 1 input
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}?")

#Calling greet_with() with Positional Arguments
greet_with("shrutu", "Nowhere")
#vs.
greet_with("Nowhere", "Jack Bauershrutu")


#Calling greet_with() with Keyword Arguments
greet_with(location="London", name="Angela")
def funcky(a="shruti",b="ayush",c=" "):
  temp=a
  a=b
  b=temp
  print(a)
  print(b)
funcky()  
def prime_check():
  is_prime=True
  for(i in range(2,number):
    if(number%i==0):
      is_prime=False
  if is_prime:
      print("prime")
  else:
      print("not prime")
      
