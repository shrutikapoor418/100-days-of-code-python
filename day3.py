# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if(year%4==0):
  if(year%100==0):
    if(year%400==0):
      print("leap ")
    else:
      print("not")
  else:
   print("leap")
else:
  print("not leap")
  
  # 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill=0
if(size=="S"):
  bill=bill+15
elif(size=="M"):
  bill=bill+20
else:
  bill=bill+25
if(add_pepperoni=="y"):
  if(size=="S"):
    bill=bill+2
  else:
    bill=bill+3
if(extra_cheese=="y"):
  bill=bill+1
print(bill)

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
namea=name1.lower()
nameb=name2.lower()
newn=name1+name2
p=newn.count("t")
q=newn.count("r")
a=newn.count("u")
b=newn.count("e")
c=newn.count("l")
d=newn.count("o")
g=newn.count("v")
h=newn.count("e")
sum=p+q+a+b
sum1=c+d+g+h
st=str(sum)
stt=str(sum1)
abc=st+stt
print(str(abc)+"%")
