print("hello")
fruits=["apple","mango","litchi","raspberry","mulberry"]
for fruit in fruits:
  print(fruit)
  # 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
s=0
c=0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  s=s+student_heights[n]
  c=c+1
av=int(s/c)
print(av)

#Write your code below this row 👇
print(student_heights)
print(sum(student_heights))
#Write your code below this row 👇
s=0
for i in range(0,100,2):
  s=s+i
print(s)
