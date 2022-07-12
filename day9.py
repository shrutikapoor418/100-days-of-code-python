student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
#TODO-1: Create an empty dictionary called student_grades.
student_grades={}


#TODO-2: Write your code below to add the grades to student_grades.👇

for i in student_scores:
  scores=student_scores[i]
  if scores >=91 and scores<=100:
    student_grades[i]="Outstanding"
  elif scores >=81 and scores<=90:
    student_grades[i]="Exceeds Expectations"
  elif scores >=71 and scores<=80:
    student_grades[i]="Acceptable"
  else:
    student_grades[i]="fail"
# 🚨 Don't change the code below 👇
print(student_grades)

#nesting lists and dictionaries

life_goals=[
  {
   "country":"usa",
    "love":["ayuu","mumma","papa","dadi","nani","bhavv"],
    "health":"100%"
  },
  {
   "company":["Google","microsoft","dell","hp"],
    "salary":"a lot 10000000000pa"
  },
]            
print(life_goals)
travel_log = [
{
  "country": "France",
  "
  from replit import clear
from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()
  visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country,visits,city):
  print(f"you have been to{country} {visits} times ")

  print(f"you have been to{city} {visits} times" )

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



#blind auction bid
from replit import clear
from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()
  





