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






