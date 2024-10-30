import time
grade_pertentage = int(input('What is the grade percentage? '))
if grade_pertentage >= 90:
    letter = ('A')
elif grade_pertentage >= 80:
    letter = ('B')
elif grade_pertentage >= 70:
    letter = ('C')
elif grade_pertentage >= 60:
    letter = ('D')
elif grade_pertentage < 60:
    letter = ('F')

sign = ""
last_digit = grade_pertentage % 10

if last_digit >= 7:
   sign = "+"
elif last_digit < 3:
   sign = "-"
else:
    sign = ""

if grade_pertentage >= 93:
    sign = ""
else:
    if grade_pertentage == "F":
        sign = ""


print(f"Your letter grade is: {letter}{sign}")

time.sleep(3)
if grade_pertentage >= 70:
    print('Congratulations!! You passed the class!')
if grade_pertentage < 70:
    print('Stay focused and you will get it nesxt time.')