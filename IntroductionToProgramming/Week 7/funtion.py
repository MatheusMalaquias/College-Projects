# # This funtion will return the first initial of a name
# def get_initial(name):
#     initial = name[0:1]
#     return initial

# # Ask for someones name and return the initials
# first_name = input('Enter your first name: ')
# first_name_initial = get_initial(first_name)

# middle_name = input('Enter your middle name: ')
# middle_name_initial = get_initial(middle_name)

# last_name = input('Enter your last name: ')
# last_name_initial = get_initial(last_name)

# print('Your initials are: ' + first_name_initial + middle_name_initial + last_name_initial)




# #O print aparece maiscula
# def get_initial(name, force_uppercase = True):
#     if force_uppercase:
#         initial = name[0:1].upper()
#     else:
#         initial = name[0:1]
#     return initial

# first_name = input('Enter your first name: ')
# first_name_initial = get_initial(first_name)

# print('Your initial is: ' + first_name_initial)

# #O print aparece minísculo
# def get_initial(name, force_uppercase = True):
#     if force_uppercase:
#         initial = name[0:1].upper()
#     else:
#         initial = name[0:1]
#     return initial

# first_name = input('Enter your first name: ')
# first_name_initial = get_initial(force_uppercase = False, name = first_name)

# print('Your initial is: ' + first_name_initial)


# #Atividade
# def display_regular(message):
#     print(message)

# def display_uppercase(message):
#     new_message = message.upper()
#     print(new_message)

# def display_lowercase(message):
#     new_message = message.lower()
#     print(new_message)

# user_message = input('What is your message? ')
# display_regular(user_message)
# display_uppercase(user_message)
# display_lowercase(user_message)

import math

def compute_area_square(side):
    return side * side

def compute_area_rectangle(length, width):
    return length * width

def compute_area_circle(radius):
    return math.pi * radius * radius

shape = ''

while shape != 'quit':
    shape = input('What shape do you have? ')
    shape = shape.lower()

    if shape == 'square':
        side = float(input('What is the length of the side? '))
        area = compute_area_square(side)
        print(f"The area is: {area}")
    elif shape == 'rectangle':
        length = float(input('What is the length? '))
        width = float(input('What is the width? '))
        area = compute_area_rectangle(length, width)
        print(f'The area is: {area}')
    elif shape == 'circle':
        radius = float(input('What is the radius? '))
        area = compute_area_circle(radius)
        print(f'The area is: {area}')