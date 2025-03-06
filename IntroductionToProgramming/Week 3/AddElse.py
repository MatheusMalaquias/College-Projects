# price = input('How much did you pay? ')
# price = float(price)

# if price >= 1.00:
#     tax = 0.7
#     print('Tax rate is: ' + str(tax))
# else:
#     tax = 0
#     print('Tax rate is: ' + str(tax))

# country = input('Enter the name of your country: ')
# if country.lower() == 'canada':
#     print('So you must like hockey!')
# else:
#     print('You are not from Canada')

# province = input('What province do you live in? ')
# tax = 0

# if province in('Alberta','Nunavut','Yukon'):
#     tax = 0.05
# elif province == 'Ontario':
#     tax = 0.13
# else:
#     tax = 0.15
# print(tax)

# country = input('What country do you live in? ')
# if country.lower() == 'canada':
#     province = input('What province/state do you live in? ')
#     if province in('Alberta','Nunavut','Yukon'):
#         tax = 0.05
#     elif province == 'Ontario':
#         tax = 0.13
#     else:
#         tax = 0.15
# else:
#     tax = 0.0
# print(tax)

# import time
# print('--------------------')
# number1 = input('What is the first number? ')
# number2 = input('What is the second number? ')
# time.sleep(3)
# if number1 > number2:
#     print('The first number is greater')
# else:
#     print('The first number is not greater')
# time.sleep(3)
# if number1 == number2:
#     print('The numbers are equal')
# else:
#     print('The numbers are not equal')
# time.sleep(3)
# if number2 > number1:
#     print('The second number is greater')
# else:
#     print('The second number is not greater')
# print('--------------------')
# animal = input('What is your favorite animal? ')
# if animal.lower() == 'horse':
#     print("That's my favorite animal too")
# else:
#     print("That one is not my favorite")

# gpa = float(input('What is your Grade Point Average? '))
# lowest_grade = float(input('What is your lowest grade? '))

# if gpa >= .85 and lowest_grade >= .70:
#     print('You made the honour roll')


# if gpa >= .85 and lowest_grade >= .70:
#     honour_roll = True
# else:
#     honour_roll = False

import time
loan_size = float(input('How large is the loan? '))
credit = float(input('How good is your credit history? '))
income = float(input('How high is your income? '))
down_payment = float(input('How large is your down payment? '))
if loan_size >= 5:
    if credit >= 7 and income >= 7:
         should_loan = True
    elif credit >= 7 or income >= 7:
        if loan_size >= 5:
           should_loan = True
        else:
            should_loan = False
    else:
        should_loan = False
else:
    if credit < 4:
        should_loan = False
    else:
        if income >= 7 or down_payment >= 7:
            should_loan = True
        elif income >= 4 and down_payment >= 4:
            should_loan = True
        else:
            should_loan = False
time.sleep(3)
if should_loan:
    print('The decision is yes. This is a good loan.')
else:
    print('The decision is no. You should not loan this money.')