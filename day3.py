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
