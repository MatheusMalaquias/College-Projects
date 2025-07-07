#import datetime

#first_name = 'Matheus'
#print('task completed')
#print(datetime.datetime.now())
#print()
#for x in range(0,10):
#    print(x)
#print(datetime.datetime.now())
#print()

#ou

#from datetime import datetime
# def print_time(task_name):
#    print(task_name)
#    print(datetime.now())
#    print()

#first_name = 'Matheus'
#print_time('first name assigned')

#for x in range(0,10):
#    print(x)
#print('loop completed')
#print(datetime.now())

#-----------------------------------------------

#first_name = input('Enter your fisrt name: ')
#first_name_initial = first_name[0:1]
#last_name = input('Enter your last name: ')
#last_name_initial = last_name[0:1]

#print('Your initials are: ' + first_name_initial + last_name_initial)

#-----------------------------------------------

# def get_initial(name):
#    initial = name[0:1].upper()
#    return  initial
#first_name = input('Enter your first name: ')
#first_name_initial = get_initial(first_name)
#last_name = input('Enter your last name: ')
#last_name_initial = get_initial(last_name)
#print('Your last name are: ' + first_name_initial \
#    + last_name_initial)

#-----------------------------------------------

# def get_initial(name):
#    initial = name[0:1].upper()
#    return  initial
#first_name = input('Enter your first name: ')
#last_name = input('Enter your last name: ')

#print('Your last name are: ' \
#    + get_initial(first_name) \
#    + get_initial(last_name))

#-----------------------------------------------

#Functions parameters

# def get_initial(name, force_uppercase):
#    if force_uppercase:
#        initial = name[0:1].upper()
#    else:
#        initial = name[0:1]
#    return  initial
#first_name = input('Enter your first name: ')
##O true or false no (first_name_initial = get_initial(first_name)) vai fazer com que o print seja minusculo ou maisculo
#first_name_initial = get_initial(first_name)

#print('Your initial is: ' + first_name_initial)

#-----------------------------------------------

#import math

#radius = float(input('Enter the radius in centimeters: '))
#height = float(input('Enter the height in centimeters: '))
#volume = math.pi * (radius**2) * height
#print(f'Volume: {volume:.2f}')

#-----------------------------------------------

#Atividade 1:

#import math
#import time

#first_odometer_miles = int(input('Enter the first odometer reading (miles): '))
#second_odometer_miles = int(input('Enter the second odometer reading (miles): '))
#fuel_used = float(input('Enter the amount of duel used (gallons): '))
#miles_per_gallon = (second_odometer_miles - first_odometer_miles) / fuel_used
#lp100k_from_mpg = 235.215 / miles_per_gallon
#time.sleep(2)
#print(f'{miles_per_gallon:.1f} miles per gallon')
#time.sleep(2)
#print(f'{lp100k_from_mpg:.2f} liters per 100 kilometers')

#-----------------------------------------------

#Atividade 2:

import math

radius = float(input('Please enter the radius of the cone: '))
height = float(input('Please enter the height of the cone: '))
volume = (math.pi * (radius ** 2) * height) / 3
print(f'Radius: {radius:.1f}')
print(f'Height: {height:.1f}')
print(f'Volume: {volume:.1f}')