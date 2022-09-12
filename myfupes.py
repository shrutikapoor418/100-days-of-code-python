#codes 1
print("enter a number");
a=input("number a please");
b=input("number b please");
if(a>b):
    print(f"{a} is big");
elif(a==b):
    print(f"{a} is equal to {b}");
else:
    print(f"{b} is big");

#even odd
print("enter a number");
c=int(input("number c please"));
if(c%2==0):
    print(f"{c} is even");
else:
    print(f"{c} is odd");
#marks avg
my_list = []
for _ in range(5):
    my_list.append(int(input("enter marks of 5 subjects")));
# Python program to find sum of elements in list
total = 0
avg=0
# Iterate each element in list
# and add them in variable total
for i in range(0, len(my_list)):
 total = total + my_list[i];
avg=total/5;
# printing total value
print("average of all elements in given list: ", avg);
#marks
mark = int(input("enter marks"));
if mark >=91 and mark<=100:
  print ("You got O Grade !!")
elif mark >=81 and mark<=90:
  print ("You got A+ Grade !!")
elif mark >=71 and mark <=80 :
  print ("You got A Grade !!")
elif mark >=61 and mark <=70 :
  print ("You got B+ Grade !!")
elif mark >=61 and mark <=70 :
  print ("You got B Grade !!")
elif mark >=51 and mark <=60 :
  print ("You got C+ Grade !!")
elif mark >=41 and mark <=50 :
  print ("You got C Grade !!")
elif mark >=35 and mark <=40 :
  print ("You got D Grade !!")
else:
  print("You failed!!")

print(15&27);
print(15|27);
print(15**27);
