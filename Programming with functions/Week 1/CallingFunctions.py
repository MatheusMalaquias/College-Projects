#Optional vs Name arguments

#last_name = input('what is your last name? ')
#first_name = input('What is your first name? ')
#major = input('What is your major? ')
#print(last_name, first_name, major, sep="|")

#Modules
#import math

#area = float(input('What is the area o the square in square inches? '))
#side = math.sqrt(area)
#print(f'The size of the a side of the square is {side}')


import math
number_items = int(input('Enter the number of items: '))
items_per_box = int(input('Enter the number of items per box: '))
boxes = math.ceil(number_items/items_per_box)
print(f'For {number_items} items, packing {items_per_box} items in each box, you will need {boxes} boxes.')