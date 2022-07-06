#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲
import random
random_int=random.randint(0,1)
if(random_int==0):
  print("tail")
else:
   print("head")
 #Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲
import random
random_int=random.randint(0,1)
if(random_int==0):
  print("tail")
else:
   print("head")

fruits=["apple","mango","grapes","cherry","guava"]
print(fruits[0])
fruits[-2]="litchi"
fruits.extend("avocado","sugarcane","papaya")
print(fruits)

""  
#Write your code below this line 👇
p=len(names)
a=random.randint(0,p-1)
pp=names[a]
print(pp+" is the person who has to pay")

#rock, paper, scissors
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
print('user info')
a=input("enter your choice:-> Rock,Paper or scissor")
t=a
if(a==0):
  print(rock)
elif(a==1):
  print(paper)
else:
  print(scissors)

lis=[rock,paper,scissors]
random_int=random.randint(0,1)
p=len(lis)
r=random.randint(0,p-1)
s=r
pp=lis[r]
print("computers' turn")
print(pp)
if(s==t):
  print("draw babe")
elif(t==0) and (s==1):
  print("computer wins")
elif(t==1) and (s==2):
  print("user wins")
elif(t==2) and (s==0):
  print("computer wins")
elif(s==0) and (t==1):
  print("user wins")
elif(s==1) and (t==2):
  print("computer wins")
elif(s==2) and (t==0):
  print("user wins")
  
  import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")
""
