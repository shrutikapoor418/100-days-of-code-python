
#Data Types
#string
print("hello"[4])
print("123"+"345")
print(2+3)
#integer
print(123+345)
#large integers
print(342_123_45+900_23_11)
#float
a=3.14159
print(a)
#boolean
num_o=len(input(":name"))
#
# print("type of num_o is"+type(num_o))
#type cast num to string
new_character=str(num_o)
# print("now  type of num_o is "+type(num_o))
print("name has "+new_character+" chars")
print(10+float("10.5"))
print(10+float("20.5")+int("1"))
print(8/3)
#floor value
print(8//3)
core=0
hei=1.8
isWinning=True
#f-String used to enter variables values too
print(f"your core is {core}, your height is {hei}, will you win?? whm i guess {isWinning}")
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
p=int(input("What was the total bill?"))
a=int(input("How much tip would you like to give? 10, 12, or 15?"))
b=int(input("How many people to split the bill?"))
tip_as_perc=int(a)/100
tot_tip_amo=int(p)*tip_as_perc
tot_bill=p+tot_tip_amo
bill_per_p=tot_bill/b
billam =round(bill_per_p,2)
print(f"Each person should pay: {billam}")
age = input("What is your current age?")#10
#Write your code below this line 

leftt=90-int(age)#80
days=365*int(leftt)
weeks=52*int(leftt)
months=12*int(leftt)
print(f"You have {days} days, {weeks} weeks, and {months} months left")

#bmi cal
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
a=float(weight)
b=float(height)
c=a/(b*b)
print(c)

